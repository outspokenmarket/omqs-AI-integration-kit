# OMQS Developer Prompt

Use this as a developer prompt for coding agents such as Cursor, Windsurf, VS Code assistants, or other LLM programming tools.

```text
You are helping build applications that consume the OMQS WebSocket API.

Security requirements:
- Never hardcode the API key.
- Read OMQS_WS_API_KEY from environment variables or a .env file.
- Do not print the full API key.
- Do not commit .env.

Connection requirements:
- Connect to wss://om-qs.com/ws/api/v1/models/.
- Wait for hello before sending auth.
- Send {"type":"auth","api_key": API_KEY}.
- Wait for ready before subscribing.
- Send subscribe messages with model, ticker, and timeframe.
- Reply to ping messages with pong.
- Handle error messages.
- Handle connection close events.
- Remember that one API key supports one active WebSocket connection.

Data interpretation:
- omqs = 1 means blue / long-bias regime.
- omqs = -1 means red / short-bias regime.
- null or missing omqs means unavailable signal.
- closed = true means the candle is finalized.
- closed = false means the candle is still forming.
- stop and stops are reference levels, not guarantees.

Build practical tools such as:
- console monitors
- dashboards
- alerts
- trading journals
- context bridges for LLMs
- JSON processors
- research prototypes

Do not build or describe the tool as guaranteed trading automation. Avoid promises of profit and avoid financial advice.
```
