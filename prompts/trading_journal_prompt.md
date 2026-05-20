# Trading Journal Prompt

Use this prompt to transform OMQS WebSocket data into a structured trading journal entry.

```text
You are helping me create a trading journal entry from OMQS WebSocket data.

OMQS is a quantitative market interpretation framework. It is not financial advice and does not promise profits.

Create a journal entry using the following fields:
- Date and time
- Symbol
- Timeframe
- Candle status
- OMQS signal
- Signal interpretation
- Close price
- Stop reference
- Fast, balanced, and slow stop levels when available
- What changed, if previous data is provided
- Risk note
- Possible follow-up observation

Interpretation rules:
- omqs = 1 means blue / long-bias regime.
- omqs = -1 means red / short-bias regime.
- null or missing means signal unavailable.
- Closed candles are more stable than open candles.
- Stop levels are references, not guarantees.

Do not provide financial advice. Do not recommend position size unless a risk framework is provided.

OMQS data:
[PASTE DATA HERE]
```
