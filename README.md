# OMQS AI Integration Kit

A practical file set that helps OMQS subscribers connect live WebSocket data with large language models.

This repository is not an autonomous trading system, not a copy trading tool, and not a replacement for risk management. It is a bridge between the **OMQS WebSocket API**, a small data-collection client, and the reasoning or generation capabilities of an LLM.

In simple terms:

```text
Python gets the data.
The LLM helps you use it.
```

---

## What this kit is

The OMQS LLM Integration Kit helps users transform raw WebSocket messages from the OMQS API into structured context that an AI assistant can understand.

The API itself provides live market data and OMQS model outputs, such as snapshots, candles, signal values, stop levels, and candle status. A normal Python client collects this data from the WebSocket API. Then the kit helps format that data into a cleaner structure that can be used by ChatGPT, Claude, Gemini, Cursor, Windsurf, VS Code agents, or other LLM-based tools.

The goal is not to make the LLM collect the data directly. The goal is to use Python, JavaScript, R, or another client to collect the data, then use an LLM to help interpret, summarize, document, automate, or build workflows around that data.

---

## The correct mental model

```text
OMQS API = live data source
Python = data collector and formatter
LLM = reasoning and generation layer
```

The LLM does not normally connect to the WebSocket API by itself. The user should use a real client, usually Python, to open the WebSocket connection, authenticate, subscribe to pairs, and receive live messages.

After that, the user can send structured context to an LLM and ask it to help create summaries, alerts, dashboards, trading journal entries, research workflows, or code.

---

## Practical workflow

The typical workflow is:

```text
OMQS WebSocket API
↓
Python client collects live snapshots and candle updates
↓
Python formats the latest market state
↓
The context bridge turns raw data into LLM-readable text or JSON
↓
The user gives that context to an LLM
↓
The LLM helps generate summaries, alerts, journals, dashboards, or research workflows
```

Or, more practically:

```text
Step 1: Use Python to connect to the OMQS WebSocket API.
Step 2: Receive live OMQS snapshots and candle updates.
Step 3: Use the context bridge to transform raw messages into structured market context.
Step 4: Send that context to an LLM.
Step 5: Ask the LLM to generate summaries, alerts, journals, dashboards, or research workflows.
```

---

## Why this exists

Raw API data is useful for developers, but many users want to do more than just print JSON messages.

They may want to ask an AI assistant to:

- explain the latest OMQS data
- summarize the current market state
- create a Discord or Telegram alert
- write a trading journal entry
- compare data across timeframes
- build a dashboard
- generate Python code around the API
- create a research workflow
- transform live data into structured reports

This kit gives the LLM enough context to understand what OMQS data means and how it should be used safely.

---

## What OMQS provides through the WebSocket API

The OMQS WebSocket API can stream real-time snapshots and live candle updates.

A typical live candle message may include:

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

The raw message is machine-readable, but it is not always ideal for an LLM or for a non-technical user.

The context bridge can turn it into something like:

```text
OMQS MARKET STATE

Symbol: BTCUSDT
Timeframe: M1
Latest close: 81012.80
Candle status: open
OMQS data: blue / long-bias regime
Default stop: 80120.55
Fast stop: 80310.10
Balanced stop: 80120.55
Slow stop: 79880.40

Interpretation context:
The model currently classifies BTCUSDT M1 as a long-bias regime.
The current candle is still open, so the data may change before the candle closes.
This should be treated as structured market context, not as a profit guarantee.
```

This is easier for an LLM to work with.

---

## How the user would use this kit

There are three practical levels of use.

### 1. Simple use: copy context into an LLM

The user opens:

```text
llm_context/COPY_THIS_TO_LLM.md
```

Then copies the content into ChatGPT, Claude, Gemini, Cursor, or another LLM.

After that, the user can ask:

```text
I want to use the OMQS WebSocket API to create an alert when BTCUSDT on 5m changes data. Use the context above and help me build the code.
```

Or:

```text
Explain how to interpret this candle received from the OMQS API.
```

Or:

```text
Create a Python script that connects to the API, reads live candles, and generates a market summary every 5 minutes.
```

In this case, the kit works as a technical memory that teaches the LLM how to understand OMQS correctly.

---

### 2. Intermediate use: collect data and transform it into LLM context

The user runs a Python client to connect to the OMQS WebSocket API.

The key example file is:

```text
examples/python_context_bridge.py
```

This script receives raw API messages and converts them into clean text that can be pasted into an LLM or passed to an AI workflow.

Instead of pasting raw JSON into the LLM, the user can generate a structured market state like:

```text
BTCUSDT M5 is currently in a blue / long-bias regime.
The latest candle is closed.
The close is 104250.50.
The default stop reference is 103640.20.
This should be interpreted as structured market context, not as a profit guarantee.
```

Then the user can ask the LLM:

```text
Based on this market state, create a concise trading journal entry.
```

Or:

```text
Transform this into a short Discord alert.
```

Or:

```text
Compare this with the higher timeframe and tell me whether there is alignment or conflict.
```

---

### 3. Advanced use: build workflows around OMQS

The `recipes/` folder contains practical workflow ideas.

Examples:

```text
recipes/build_a_market_monitor.md
recipes/build_a_signal_dashboard.md
recipes/build_a_trading_journal.md
recipes/build_a_discord_alert_bot.md
recipes/build_an_ai_market_assistant.md
```

These recipes help users build real tools around the OMQS WebSocket API.

For example, the user can open:

```text
recipes/build_a_discord_alert_bot.md
```

Then ask an LLM:

```text
Use this recipe and help me create a Discord bot that sends an alert when OMQS changes from red to blue on BTCUSDT M5.
```

Or open:

```text
recipes/build_a_trading_journal.md
```

And ask:

```text
Create a simple system that records each OMQS data change into a CSV file for later review.
```

---

## Repository structure

```text
omqs-llm-integration-kit/
│
├── README.md
├── .env.example
├── .gitignore
├── requirements.txt
│
├── docs/
│   ├── OMQS_WEBSOCKET_API.md
│   ├── OMQS_SIGNAL_INTERPRETATION.md
│   ├── OMQS_LIMITS_AND_ERRORS.md
│   └── OMQS_SAFETY_AND_USAGE_GUIDE.md
│
├── llm_context/
│   ├── COPY_THIS_TO_LLM.md
│   ├── OMQS_LLM_CONTEXT.md
│   ├── OMQS_SYSTEM_PROMPT.md
│   ├── OMQS_DEVELOPER_PROMPT.md
│   ├── OMQS_USER_PROMPT_TEMPLATE.md
│   └── OMQS_JSON_SCHEMAS.md
│
├── prompts/
│   ├── market_monitor_prompt.md
│   ├── signal_explainer_prompt.md
│   ├── trading_journal_prompt.md
│   ├── strategy_research_prompt.md
│   └── alert_builder_prompt.md
│
├── examples/
│   ├── python_console_client.py
│   ├── python_context_bridge.py
│   ├── python_notebook_client.ipynb
│   ├── sample_snapshot.json
│   ├── sample_candle.json
│   └── sample_llm_analysis.md
│
└── recipes/
    ├── build_a_market_monitor.md
    ├── build_a_signal_dashboard.md
    ├── build_a_trading_journal.md
    ├── build_a_discord_alert_bot.md
    └── build_an_ai_market_assistant.md
```

---

## Important files

### `llm_context/COPY_THIS_TO_LLM.md`

This is the fastest way to start.

Copy this file into an LLM before asking it to help with OMQS API workflows. It gives the model the correct context, terminology, safety boundaries, and data structure.

### `examples/python_console_client.py`

A simple Python client that connects to the OMQS WebSocket API and prints live data.

### `examples/python_context_bridge.py`

The most important bridge file. It converts raw OMQS messages into structured context that an LLM can understand.

### `docs/OMQS_SIGNAL_INTERPRETATION.md`

Explains how to think about OMQS data as market-regime or directional-bias information, not as guaranteed predictions.

### `recipes/`

Practical guides for turning OMQS API data into real workflows such as alerts, dashboards, journals, and AI assistants.

---

## Installation

Create and activate your Python environment, then install the requirements:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```text
OMQS_WS_API_KEY=your_websocket_api_key_here
OMQS_WS_URL=wss://om-qs.com/ws/api/v1/models/
```

Never commit your real `.env` file to GitHub.

---

## Example usage

Run the console client:

```bash
python examples/python_console_client.py
```

Run the context bridge:

```bash
python examples/python_context_bridge.py
```

Then copy the generated market context and paste it into your preferred LLM.

Example prompt:

```text
Here is the latest OMQS market context. Summarize it in a professional way and create a short alert message suitable for Discord. Do not give financial advice or promise profits.
```

---

## What users can build

With this kit, users can build:

- AI market assistants
- data dashboards
- Discord or Telegram alerts
- trading journals
- market summaries
- quant research workflows
- LLM-readable market reports
- custom automations around OMQS data

---

## Data interpretation

The OMQS data should be understood as structured quantitative market context.

A simplified interpretation is:

```text
omqs = 1   → blue / long-bias regime
omqs = -1  → red / short-bias regime
null        → data unavailable
```

Important notes:

- A blue signal is not a guarantee that price will rise.
- A red signal is not a guarantee that price will fall.
- An open candle can still change before closing.
- Closed candles are usually more stable for decision-support workflows.
- Stop levels are risk references, not profit guarantees.
- OMQS is not financial advice.

---

## Safety and positioning

This repository is designed for education, research, monitoring, and decision-support workflows.

Do not present OMQS as:

- copy trading
- a guaranteed trading system
- an execution platform
- financial advice
- a promise of future performance
- a replacement for risk management

Better framing:

```text
Use OMQS WebSocket data as structured real-time context for AI assistants, dashboards, alerts, trading journals, and quantitative workflows.
```

---

## One-line explanation

```text
Python collects the live OMQS data. The LLM helps you understand it, summarize it, and build useful workflows around it.
```

---

## Learn more

Visit:

```text
https://om-qs.com
```

