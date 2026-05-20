# Recipe: Build a Discord Alert Bot

This recipe explains how to use OMQS WebSocket data to create Discord alerts.

## Goal

Send Discord alerts when relevant OMQS conditions occur.

Example alert conditions:

- A candle closes with `omqs = 1`.
- A candle closes with `omqs = -1`.
- OMQS changes from red to blue.
- OMQS changes from blue to red.
- Close is above or below a stop reference.
- Higher and lower timeframes align.

## Recommended alert rules

Start with closed candle alerts:

```text
Trigger only when closed = true.
```

This avoids excessive alerts from still-forming candles.

## Example alert text

```text
OMQS Alert: BTCUSDT M5
Closed candle confirmed: blue / long-bias regime
Close: 81012.80
Balanced stop: 80120.55
Note: This is quantitative market context, not financial advice.
```

## Example JSON payload

```json
{
  "content": "OMQS Alert: BTCUSDT M5\nClosed candle confirmed: blue / long-bias regime\nClose: 81012.80\nBalanced stop: 80120.55\nNote: This is quantitative market context, not financial advice."
}
```

## LLM extension

You can ask an LLM to convert an OMQS candle into a human-readable alert message.

Use:

```text
Create a concise Discord alert from this OMQS candle. Do not provide financial advice. Mention whether the candle is closed and include stop context.
```

## Safety note

Avoid messages such as:

```text
Buy now. Guaranteed move.
```

Prefer:

```text
Closed candle confirmed a blue long-bias regime according to OMQS.
```
