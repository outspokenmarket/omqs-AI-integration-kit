# OMQS WebSocket API

Real-time market snapshots and live candle updates from OMQS models over WebSocket.

## Overview

- Included in the user's subscription.
- Does not consume REST API credits.
- Uses a dedicated WebSocket API key.
- Users without an active subscription cannot access the WebSocket API.
- The WebSocket API has limits separate from the web UI and mobile app.
- REST legacy API keys are not affected by WebSocket key regeneration.

## Connection URL

```text
wss://om-qs.com/ws/api/v1/models/
```

## Authentication flow

Open the WebSocket connection and wait for the server `hello` message. Then send an `auth` message:

```json
{
  "type": "auth",
  "api_key": "your_websocket_api_key_here"
}
```

Access rules:

- API key must exist and be active.
- Current API terms must be accepted.
- User must have an active subscription.
- Authentication must happen within 10 seconds.
- Send the `auth` message after `hello`.
- Each API key supports one active WebSocket connection.
- Opening a new connection with the same key replaces the previous connection.

## Connection lifecycle

| Message | Origin | Behavior |
| --- | --- | --- |
| `hello` | Server | First message after connection accept. It announces that authentication is required. |
| `auth` | Client | Sends the WebSocket API key. |
| `ready` | Server | Confirms authentication and returns effective limits. The value 83 in limits is informational, not an error. |
| `subscribe` | Client | Registers active pairs and receives an initial snapshot. Additional subscribes accumulate active pairs until unsubscribe is sent. |
| `subscribed` | Server | Confirms subscription and returns normalized active pairs. |
| `snapshot` | Server | Initial compact snapshot with up to 10 candles per pair. |
| `candle` | Server | Live candle update, open or closed. |
| `unsubscribe` | Client | Removes one, more, or all active pairs. |
| `unsubscribed` | Server | Confirms unsubscribe and returns remaining active pair count. |
| `ping` | Server | Heartbeat message sent approximately every 30 seconds. |
| `pong` | Client | Required response to keep the connection alive. |

## Subscribe message

```json
{
  "type": "subscribe",
  "request_id": "sub-main",
  "pairs": [
    { "model": "crypto", "ticker": "BTCUSDT", "timeframe": "1m" },
    { "model": "crypto", "ticker": "ETHUSDT", "timeframe": "5m" },
    { "model": "forex", "ticker": "EURUSD", "timeframe": "5m" }
  ]
}
```

## Unsubscribe one or more pairs

```json
{
  "type": "unsubscribe",
  "request_id": "unsub-btc",
  "pairs": [
    { "model": "crypto", "ticker": "BTCUSDT", "timeframe": "1m" }
  ]
}
```

## Unsubscribe all pairs

```json
{
  "type": "unsubscribe",
  "request_id": "unsub-all",
  "all": true
}
```

## Ready message

```json
{
  "type": "ready",
  "connection_id": "4ccf6f8f5b2c46bb9ac8a72e4d347b65",
  "client_kind": "websocket_api",
  "identity": "api_key:123",
  "limits": {
    "max_pairs_per_connection": 83,
    "max_pairs_per_user": 83,
    "max_connections_per_api_key": 1
  }
}
```

## Snapshot message

A snapshot contains up to 10 recent candles for a subscribed pair:

```json
{
  "type": "snapshot",
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "ohlc": [
    {
      "timestamp": 1774915200,
      "open": "80920.00",
      "high": "81020.00",
      "low": "80880.00",
      "close": "80988.41",
      "volume": "24.18",
      "closed": true,
      "omqs": 1,
      "stop": "80120.55",
      "stops": {
        "fast": "80310.10",
        "balanced": "80120.55",
        "slow": "79880.40"
      }
    }
  ],
  "omqs": 1,
  "stop": "80120.55",
  "stops": {
    "fast": "80310.10",
    "balanced": "80120.55",
    "slow": "79880.40"
  }
}
```

## Live candle message

```json
{
  "type": "candle",
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "timestamp": 1774915260,
  "open": "80988.41",
  "high": "81044.20",
  "low": "80970.00",
  "close": "81012.80",
  "volume": "18.42",
  "closed": false,
  "omqs": 1,
  "stop": "80120.55",
  "stops": {
    "fast": "80310.10",
    "balanced": "80120.55",
    "slow": "79880.40"
  }
}
```

## Supported model examples

| model | ticker | timeframe |
| --- | --- | --- |
| `crypto` | `BTCUSDT` | `1m`, `5m`, `15m`, or enabled timeframe |
| `forex` | `EURUSD` | `1m`, `5m`, `15m`, or enabled timeframe |
| `b3_futures` | `WDO` | enabled timeframe |
| `b3_stocks` | `PETR4` | enabled timeframe |
| `nasdaq` | `AAPL` | enabled timeframe |
| `international` | `SPY` | enabled timeframe |
| `us_futures` | `ES` | enabled timeframe |
