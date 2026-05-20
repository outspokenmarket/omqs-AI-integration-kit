# OMQS User Prompt Template

Use this template when asking an LLM to analyze OMQS data.

```text
I am using the OMQS WebSocket API.

Please analyze the following OMQS market state.

Important rules:
- Treat OMQS as a quantitative regime signal.
- Do not provide financial advice.
- Do not promise profits.
- Do not treat the signal as a guaranteed prediction.
- Distinguish open candles from closed candles.
- Use stop levels as reference context only.

Task:
[Describe what you want: summary, alert, journal, dashboard text, JSON output, strategy research note, etc.]

OMQS data:
[Paste snapshot, candle, or generated market state here]

Output format:
[Choose: concise paragraph, bullet list, JSON, alert message, journal entry, dashboard copy, etc.]
```

## Example

```text
I am using the OMQS WebSocket API.

Please create a concise Discord alert from the following OMQS candle.

Important rules:
- Treat OMQS as a quantitative regime signal.
- Do not provide financial advice.
- Do not promise profits.
- Distinguish open candles from closed candles.
- Use stop levels as reference context only.

OMQS data:
{
  "type": "candle",
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "close": "81012.80",
  "closed": true,
  "omqs": 1,
  "stop": "80120.55"
}

Output format:
One concise Discord message.
```
