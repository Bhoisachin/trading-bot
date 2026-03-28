# Binance Futures Testnet Trading Bot

## Features
- Place MARKET and LIMIT orders
- Supports BUY / SELL
- CLI-based interface (Typer)
- Input validation
- Logging of API requests/responses
- Error handling
- Order execution tracking

---

## Run commands

### Market Order 
 ```bash py -m cli BTCUSDT BUY MARKET 0.002  ```
---
### Limited order 
 ```bash python -m cli BTCUSDT SELL LIMIT 0.002 --price 60000 ```

## Logs
```bash logs/app.log ```

---
## Setup

```bash
git clone <repo>
cd trading-bot
pip install -r requirements.txt ```



