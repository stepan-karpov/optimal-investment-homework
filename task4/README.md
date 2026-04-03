# KR1 Задача №4 — Freqtrade

**Фамилия:** Карпов  

**Что реализовано:**
- **strategy1**: Три красные свечи подряд → открываем **только short** (вариант 4)
- **strategy2**: Индикатор RSI (уровни 70/30) → long и short (вариант 4)
- Инструмент: фьючерс **ETH/USDT**
- Таймфрейм: **1 день**
- Биржа: **Kraken**
- Выход из позиции: **ровно через 48 часов** (2 свечи на 1d)
- Период бэктеста: 2023-01-01 — 2025-12-31

**Как запускать:**

```bash
# Strategy 1
freqtrade backtesting --strategy Strategy1 --config strategy1/config.json

# Strategy 2
freqtrade backtesting --strategy Strategy2 --config strategy2/config.json
```