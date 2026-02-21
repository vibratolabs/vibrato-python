import asyncio
import inspect
import json
from typing import Any, AsyncIterator, Callable, Dict, Optional
from urllib.parse import urlencode, urlparse, urlunparse

import websockets


class TranscriptStreamError(Exception):
    """Base error for transcript websocket streaming."""


class AuthenticationError(TranscriptStreamError):
    """Raised when API key authentication fails (close code 4401)."""


class ForbiddenError(TranscriptStreamError):
    """Raised when the API key does not have access (close code 4403)."""


class NotFoundError(TranscriptStreamError):
    """Raised when the call cannot be found or is not owned (close code 4404)."""


class ConnectionClosedError(TranscriptStreamError):
    """Raised for unexpected websocket close events."""


class TranscriptStream:
    """Client for live transcript events from the public websocket endpoint."""

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        if not api_key:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.base_url = base_url or "https://api.getvibrato.com"
        self._websocket: Any = None

    @staticmethod
    def _to_ws_scheme(url: str) -> str:
        parsed = urlparse(url)
        scheme = parsed.scheme.lower()
        if scheme == "https":
            new_scheme = "wss"
        elif scheme == "http":
            new_scheme = "ws"
        elif scheme in {"ws", "wss"}:
            new_scheme = scheme
        else:
            raise ValueError(f"Unsupported base_url scheme: {parsed.scheme}")
        return urlunparse((new_scheme, parsed.netloc, parsed.path, "", "", ""))

    @staticmethod
    def _normalize_base_path(path: str) -> str:
        normalized = path.rstrip("/")
        # Accept API base URLs from the REST SDK and strip versioned API prefixes.
        if normalized.endswith("/api/v1"):
            normalized = normalized[: -len("/api/v1")]
        elif normalized.endswith("/api"):
            normalized = normalized[: -len("/api")]
        return normalized

    def _build_ws_url(self, call_id: str, use_query_param: bool = False) -> str:
        if not call_id:
            raise ValueError("call_id is required")

        ws_base = self._to_ws_scheme(self.base_url)
        parsed = urlparse(ws_base)
        base_path = self._normalize_base_path(parsed.path)
        path = f"{base_path}/api/ws/public/calls/{call_id}/transcript"

        query = ""
        if use_query_param:
            query = urlencode({"api_key": self.api_key})

        return urlunparse((parsed.scheme, parsed.netloc, path, "", query, ""))

    @staticmethod
    def _connection_kwargs(api_key: str, use_query_param: bool) -> Dict[str, Any]:
        if use_query_param:
            return {}

        headers = {"Authorization": f"Bearer {api_key}"}
        signature = inspect.signature(websockets.connect)
        if "additional_headers" in signature.parameters:
            return {"additional_headers": headers}
        return {"extra_headers": headers}

    @staticmethod
    def _map_close_code(code: Optional[int], reason: str) -> Exception:
        if code == 4401:
            return AuthenticationError("Unauthorized websocket API key")
        if code == 4403:
            return ForbiddenError("API key does not have websocket access")
        if code == 4404:
            return NotFoundError("Call not found or not accessible")
        return ConnectionClosedError(
            f"Websocket closed unexpectedly (code={code}, reason={reason})"
        )

    async def connect(
        self, call_id: str, use_query_param: bool = False
    ) -> AsyncIterator[Dict[str, Any]]:
        """Yield transcript websocket events as they arrive."""
        url = self._build_ws_url(call_id, use_query_param=use_query_param)
        kwargs = self._connection_kwargs(self.api_key, use_query_param)

        try:
            async with websockets.connect(url, **kwargs) as websocket:
                self._websocket = websocket
                async for raw_msg in websocket:
                    payload = json.loads(raw_msg)
                    if isinstance(payload, dict):
                        yield payload
        except Exception as exc:
            code = getattr(exc, "code", None)
            reason = getattr(exc, "reason", str(exc))
            if code is not None:
                raise self._map_close_code(code, reason)
            raise
        finally:
            self._websocket = None

    def listen(
        self,
        call_id: str,
        on_event: Callable[[Dict[str, Any]], None],
        use_query_param: bool = False,
    ) -> None:
        """Listen for events in a synchronous context and call on_event for each one."""
        if on_event is None:
            raise ValueError("on_event callback is required")

        async def _runner() -> None:
            async for event in self.connect(call_id, use_query_param=use_query_param):
                on_event(event)

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            raise RuntimeError(
                "listen() cannot run inside an active event loop. "
                "Use 'async for event in stream.connect(...)' instead."
            )

        asyncio.run(_runner())

    async def close(self) -> None:
        """Close an active websocket connection if present."""
        if self._websocket is not None:
            await self._websocket.close()
