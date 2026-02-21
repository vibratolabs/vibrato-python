# Transcript Streaming

Use a snapshot-plus-stream pattern for reliable transcript state:

1. Fetch a full snapshot over REST with `s.calls.get_transcript(id=...)`
2. Subscribe to live events over websocket with `TranscriptStream`

This avoids missing messages across reconnects and process restarts.

## Install

```bash
pip install -e ".[dev]"
```

Runtime dependency:

- `websockets>=12.0`

## Quick Start (Async)

```python
import asyncio
import vibrato
from vibrato.transcript_stream import TranscriptStream


async def main():
    api_key = "<YOUR_API_KEY>"
    call_id = "123"

    sdk = vibrato.Vibrato(bearer_auth=api_key)
    snapshot_res = sdk.calls.get_transcript(id=call_id)
    messages = (snapshot_res.transcript.messages or []) if snapshot_res.transcript else []
    print(f"Snapshot messages: {len(messages)}")

    stream = TranscriptStream(api_key=api_key)
    async for event in stream.connect(call_id):
        event_type = event.get("event_type")
        if event_type == "transcript_snapshot":
            print("WS snapshot", len(event.get("messages", [])))
        elif event_type == "transcript_message":
            print("New message", event.get("message", {}))


asyncio.run(main())
```

## Quick Start (Sync Callback)

```python
from vibrato.transcript_stream import TranscriptStream


def on_event(event):
    print(event)


stream = TranscriptStream(api_key="<YOUR_API_KEY>")
stream.listen(call_id="123", on_event=on_event)
```

## Authentication

Default behavior uses header auth:

- `Authorization: Bearer <api_key>`

For environments where custom websocket headers are not supported, use query param fallback:

```python
async for event in stream.connect(call_id="123", use_query_param=True):
    ...
```

This connects using `?api_key=<api_key>`.

## Event Format

### `transcript_snapshot`

Sent immediately after connect with full current transcript state.

```json
{
  "event_type": "transcript_snapshot",
  "messages": [
    {
      "content": "Hello",
      "speaker": "Human",
      "created_at": "2026-02-21T12:00:00Z",
      "finalized_at": "2026-02-21T12:00:01Z"
    }
  ]
}
```

### `transcript_message`

Sent for each new message after subscription.

```json
{
  "event_type": "transcript_message",
  "message": {
    "content": "Hi there",
    "speaker": "AI",
    "created_at": "2026-02-21T12:00:02Z",
    "finalized_at": "2026-02-21T12:00:03Z"
  }
}
```

## Errors

The client maps websocket close codes to typed exceptions:

- `4401` -> `AuthenticationError`
- `4403` -> `ForbiddenError`
- `4404` -> `NotFoundError`
- other codes -> `ConnectionClosedError`

## Production Guidance

- Always initialize local state from REST snapshot before applying stream events.
- On disconnect, reconnect and treat the next `transcript_snapshot` as source of truth.
- If using query-param auth, avoid logging full websocket URLs.
- Keep API keys server-side whenever possible.
