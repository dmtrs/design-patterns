# Strategies

Inspired from the [Pine Script v4 User Manual](https://www.tradingview.com/pine-script-docs/en/v4/essential/Strategies.html)(© Copyright 2022, TradingView.).

We propose a `python` api implementation for 
>  A `strategy` ... that can send, modify and cancel buy/sell orders.

Starting with the simple strategy example:
```
//@version=4
strategy("test")
if bar_index < 100
    strategy.entry("buy", strategy.long, 10, when=strategy.position_size <= 0)
    strategy.entry("sell", strategy.short, 10, when=strategy.position_size > 0)
plot(strategy.equity)
```

## Order and entry

- `strategy.entry`: command to enter market position
- `strategy.order`: command to place order

> If an order with the same ID is already pending, it is possible to modify the order. 
