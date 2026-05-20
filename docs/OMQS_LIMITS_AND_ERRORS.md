# OMQS Limits and Errors

This document summarizes the main operational limits, close codes, and API error messages for the OMQS WebSocket API.

## Main limits

| Item | Value | Detail |
| --- | --- | --- |
| WebSocket keys per user | 1 active | Generating a new key revokes the previous WebSocket key. Legacy REST keys are not affected. |
| Connections per API key | 1 | A new connection with the same key replaces the previous one. |
| Pairs per connection | 83 | Maximum active pairs in one WebSocket API connection. |
| Pairs per user on WebSocket API | 83 | Separate from web UI and mobile app limits. |
| Subscription changes | 30 per minute | Applies to subscribe and unsubscribe messages. |
| Heartbeat | 30s ping / 90s timeout | The client must reply with pong before timeout. |

## Close codes

| Close code | Code | Meaning |
| --- | --- | --- |
| `4001` | `connection_replaced` | The same API key opened another connection and the previous one was closed. |
| `4401` | `auth_timeout` or invalid credential | Authentication did not happen in time, the key was invalid, or the key was revoked. |
| `4403` | `subscription_required` | The user does not have an active subscription. |
| `4408` | `heartbeat_timeout` | The client did not reply to server pings in time. |
| `4013` | `capacity_limit` | Pair, connection, user, or process capacity was exceeded. |

## Error codes

| Error code | Meaning |
| --- | --- |
| `invalid_json` | Message is not valid JSON. |
| `invalid_message` | JSON message is not an object. |
| `unsupported_type` | Missing or unsupported `type`. |
| `authentication_required` | Subscribe or unsubscribe was sent before authentication. |
| `already_authenticated` | Auth was sent more than once in the same connection. |
| `invalid_subscription` | Subscribe contains invalid pairs, model, ticker, or timeframe. |
| `invalid_unsubscribe` | Unsubscribe contains invalid pairs, model, ticker, or timeframe. |
| `rate_limited` | More than 30 subscribe or unsubscribe changes per minute. |
| `snapshot_unavailable` | Initial snapshot is unavailable for the requested pair. |
| `connection_replaced` | Another connection used the same API key. |
| `api_key_revoked` | The key was revoked by regenerate or revoke. |
| `heartbeat_timeout` | Client did not reply to server ping messages. |
| `capacity_limit` | A configured limit was exceeded. |

## Example capacity error

```json
{
  "type": "error",
  "code": "capacity_limit",
  "message": "WebSocket API capacity limit reached: max_pairs_per_connection.",
  "request_id": "sub-83-pairs",
  "detail": {
    "reason": "max_pairs_per_connection",
    "requested_pairs": 84,
    "max_pairs_per_connection": 83,
    "max_pairs_per_user": 83
  }
}
```

## Common troubleshooting

### I see 83 in the ready message. Is it an error?

No. The number 83 in `ready.limits` is informational. It tells you the maximum number of active pairs allowed in the connection.

### My old notebook keeps disconnecting

The WebSocket API allows one active connection per key. If you run the same notebook cell twice, the newest connection may replace the previous one. Restart the notebook kernel before opening a new connection if needed.

### I receive heartbeat timeout

Make sure your client responds to every server `ping` message with:

```json
{"type":"pong"}
```

### Subscribe is rejected

Check:

- model name
- ticker format
- timeframe format
- active subscription status
- pair limit
- rate limit
