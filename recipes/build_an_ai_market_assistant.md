# Recipe: Build an AI Market Assistant

This recipe explains how to build an AI assistant that uses OMQS WebSocket data as structured real-time context.

## Goal

Create an assistant that can:

- Read OMQS market state
- Summarize signals
- Explain stop context
- Compare assets and timeframes
- Create alerts
- Create journal entries
- Produce dashboard summaries
- Help with research workflows

## Recommended architecture

```text
OMQS WebSocket API
↓
Python client
↓
Normalized market state
↓
Text context bridge
↓
LLM prompt
↓
Summary, alert, journal, dashboard, or research note
```

## Step 1: Consume the API

Use `examples/python_console_client.py` to receive live OMQS messages.

## Step 2: Normalize the message

Convert each candle into a stable structure:

```json
{
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "close": 81012.8,
  "closed": false,
  "omqs": 1,
  "signal_label": "blue / long-bias regime",
  "stop": 80120.55,
  "stop_fast": 80310.1,
  "stop_balanced": 80120.55,
  "stop_slow": 79880.4
}
```

## Step 3: Convert to LLM-readable text

Use `examples/python_context_bridge.py` to produce text such as:

```text
BTCUSDT M1 is currently in a blue long-bias regime. The candle is still open, so the signal should be treated as live market context rather than finalized confirmation. The default stop reference is 80120.55.
```

## Step 4: Apply a prompt

Use one of the prompt files:

- `prompts/market_monitor_prompt.md`
- `prompts/signal_explainer_prompt.md`
- `prompts/trading_journal_prompt.md`
- `prompts/strategy_research_prompt.md`
- `prompts/alert_builder_prompt.md`

## Step 5: Output structured results

Useful assistant outputs:

- A concise market summary
- A JSON object for automation
- A Discord alert
- A trading journal entry
- A dashboard explanation
- A research note

## Safety behavior

The AI assistant should always remember:

- OMQS is decision-support context.
- OMQS is not financial advice.
- OMQS does not guarantee future price movement.
- Stop levels are references, not promises.
- Open candles can change before closing.
