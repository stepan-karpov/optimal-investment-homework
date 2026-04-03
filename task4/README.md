# KR1 Задача №4 — Freqtrade

**Фамилия:** Карпов  

**Что реализовано:**
- **strategy1**: Три красные свечи подряд - открываем **только short** (вариант 4)
- **strategy2**: Индикатор RSI (уровни 70/30) - long и short (вариант 4)
- Инструмент: фьючерс **ETH/USDT**
- Таймфрейм: **1 день**
- Биржа: **OKX**
- Условие выхода: закрытие позиции **ровно через 48 часов** (2 свечи на 1d)
- Период бэктеста: 2023-01-01 — 2025-12-31

**Как запускать:**

```bash
freqtrade download-data \
  --exchange okx \
  --pairs ETH/USDT:USDT \
  --timeframe 1d \
  --timerange 20230101-20251231 \
  --trading-mode futures

# Strategy 1
freqtrade backtesting \
  --strategy Strategy1 \
  --config strategy1/config.json \
  --strategy-path ./strategy1 \
  | tee strategy1/backtest_results.txt

cp strategy1/strategy1.py user_data/strategies/Strategy1.py
freqtrade webserver --config strategy1/config.json

# Strategy 2
freqtrade backtesting \
  --strategy Strategy2 \
  --config strategy2/config.json \
  --strategy-path ./strategy2 \
  | tee strategy2/backtest_results.txt

cp strategy2/strategy2.py user_data/strategies/Strategy2.py
freqtrade webserver --config strategy2/config.json
```