# Alert Builder Prompt

Use this prompt to ask an LLM to create alert rules and alert messages from OMQS WebSocket data.

```text
You are helping me build alerts from OMQS WebSocket data.

OMQS is a quantitative market interpretation system. It is not copy trading, not financial advice, not an execution platform, and not a promise of profit.

Interpret OMQS as:
- omqs = 1 means blue / long-bias regime.
- omqs = -1 means red / short-bias regime.
- null or missing means signal unavailable.

Create alert logic and alert messages based on the data below.

Rules:
- Prefer closed candles for stronger confirmation alerts.
- Mention if the candle is still open.
- Use stop levels as reference context.
- Do not say guaranteed profit.
- Do not say buy now or sell now.
- Produce clean alert text suitable for Discord, Telegram, Slack, or email.

Please provide:
1. Alert condition
2. Alert message
3. Optional JSON payload
4. Risk and uncertainty note

OMQS data:
[PASTE DATA HERE]
```
