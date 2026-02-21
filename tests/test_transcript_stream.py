import json
from unittest.mock import AsyncMock, Mock, patch

import pytest

from vibrato.transcript_stream import (
    AuthenticationError,
    ConnectionClosedError,
    ForbiddenError,
    NotFoundError,
    TranscriptStream,
)


class DummyCloseError(Exception):
    def __init__(self, code, reason="closed"):
        self.code = code
        self.reason = reason
        super().__init__(reason)


class FakeWebSocket:
    def __init__(self, messages=None, error=None):
        self._messages = messages or []
        self._error = error
        self.close = AsyncMock()

    def __aiter__(self):
        async def _gen():
            for message in self._messages:
                yield message
            if self._error is not None:
                raise self._error

        return _gen()


class FakeConnectContext:
    def __init__(self, websocket):
        self.websocket = websocket

    async def __aenter__(self):
        return self.websocket

    async def __aexit__(self, exc_type, exc, tb):
        return False


@pytest.mark.asyncio
async def test_auth_header_construction_uses_bearer_header():
    stream = TranscriptStream(api_key="test-key")
    fake_ws = FakeWebSocket(
        messages=[json.dumps({"event_type": "transcript_snapshot", "messages": []})]
    )
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        events = [event async for event in stream.connect("123")]

    assert len(events) == 1
    called_url = connect_mock.call_args.args[0]
    called_kwargs = connect_mock.call_args.kwargs
    assert called_url == "wss://api.getvibrato.com/api/ws/public/calls/123/transcript"
    assert "api_key=" not in called_url

    header_key = (
        "additional_headers"
        if "additional_headers" in called_kwargs
        else "extra_headers"
    )
    assert called_kwargs[header_key] == {"Authorization": "Bearer test-key"}


@pytest.mark.asyncio
async def test_query_param_fallback_puts_api_key_in_url():
    stream = TranscriptStream(api_key="test-key")
    fake_ws = FakeWebSocket(
        messages=[json.dumps({"event_type": "transcript_snapshot", "messages": []})]
    )
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        events = [event async for event in stream.connect("123", use_query_param=True)]

    assert len(events) == 1
    called_url = connect_mock.call_args.args[0]
    called_kwargs = connect_mock.call_args.kwargs
    assert called_url.endswith("/api/ws/public/calls/123/transcript?api_key=test-key")
    assert "additional_headers" not in called_kwargs
    assert "extra_headers" not in called_kwargs


@pytest.mark.asyncio
async def test_ws_url_construction_for_custom_and_http_base_url():
    stream_https = TranscriptStream(api_key="k", base_url="https://example.com/root")
    stream_http = TranscriptStream(api_key="k", base_url="http://localhost:8000")
    stream_api_v1 = TranscriptStream(api_key="k", base_url="https://example.com/api/v1")

    assert (
        stream_https._build_ws_url("7")
        == "wss://example.com/root/api/ws/public/calls/7/transcript"
    )
    assert (
        stream_http._build_ws_url("8")
        == "ws://localhost:8000/api/ws/public/calls/8/transcript"
    )
    assert (
        stream_api_v1._build_ws_url("9")
        == "wss://example.com/api/ws/public/calls/9/transcript"
    )


@pytest.mark.asyncio
async def test_snapshot_event_yields_expected_payload():
    snapshot = {"event_type": "transcript_snapshot", "messages": []}
    fake_ws = FakeWebSocket(messages=[json.dumps(snapshot)])
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))
    stream = TranscriptStream(api_key="k")

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        events = [event async for event in stream.connect("call-id")]

    assert events == [snapshot]


@pytest.mark.asyncio
async def test_stream_events_arrive_in_order():
    messages = [
        json.dumps(
            {
                "event_type": "transcript_message",
                "message": {
                    "content": "Hello",
                    "speaker": "Human",
                    "created_at": "2026-02-21T12:00:00Z",
                    "finalized_at": "2026-02-21T12:00:01Z",
                },
            }
        ),
        json.dumps(
            {
                "event_type": "transcript_message",
                "message": {
                    "content": "Hi there",
                    "speaker": "AI",
                    "created_at": "2026-02-21T12:00:02Z",
                    "finalized_at": "2026-02-21T12:00:03Z",
                },
            }
        ),
    ]
    fake_ws = FakeWebSocket(messages=messages)
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))
    stream = TranscriptStream(api_key="k")

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        events = [event async for event in stream.connect("call-id")]

    assert events[0]["message"]["content"] == "Hello"
    assert events[1]["message"]["content"] == "Hi there"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "close_code,expected_error",
    [
        (4401, AuthenticationError),
        (4403, ForbiddenError),
        (4404, NotFoundError),
    ],
)
async def test_close_code_mapping(close_code, expected_error):
    fake_ws = FakeWebSocket(error=DummyCloseError(close_code, "boom"))
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))
    stream = TranscriptStream(api_key="k")

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        with pytest.raises(expected_error):
            _ = [event async for event in stream.connect("call-id")]


@pytest.mark.asyncio
async def test_unexpected_close_code_raises_generic_connection_error():
    fake_ws = FakeWebSocket(error=DummyCloseError(1006, "abnormal"))
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))
    stream = TranscriptStream(api_key="k")

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        with pytest.raises(ConnectionClosedError):
            _ = [event async for event in stream.connect("call-id")]


def test_sync_listen_calls_callback_for_each_event():
    callback = Mock()
    events = [
        json.dumps({"event_type": "transcript_snapshot", "messages": []}),
        json.dumps(
            {
                "event_type": "transcript_message",
                "message": {"content": "a"},
            }
        ),
        json.dumps(
            {
                "event_type": "transcript_message",
                "message": {"content": "b"},
            }
        ),
    ]
    fake_ws = FakeWebSocket(messages=events)
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))
    stream = TranscriptStream(api_key="k")

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        stream.listen("call-id", callback)

    assert callback.call_count == 3
    assert callback.call_args_list[0].args[0]["event_type"] == "transcript_snapshot"
    assert callback.call_args_list[1].args[0]["message"]["content"] == "a"
    assert callback.call_args_list[2].args[0]["message"]["content"] == "b"


@pytest.mark.asyncio
async def test_close_calls_websocket_close_when_present():
    stream = TranscriptStream(api_key="k")
    fake_ws = FakeWebSocket()
    stream._websocket = fake_ws

    await stream.close()

    fake_ws.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_empty_snapshot_is_supported():
    fake_ws = FakeWebSocket(
        messages=[json.dumps({"event_type": "transcript_snapshot", "messages": []})]
    )
    connect_mock = Mock(return_value=FakeConnectContext(fake_ws))
    stream = TranscriptStream(api_key="k")

    with patch("vibrato.transcript_stream.websockets.connect", connect_mock):
        events = [event async for event in stream.connect("call-id")]

    assert events == [{"event_type": "transcript_snapshot", "messages": []}]
