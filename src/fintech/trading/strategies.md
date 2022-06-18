# Strategies

Inspired from the [Pine Script v4 User Manual](https://www.tradingview.com/pine-script-docs/en/v4/essential/Strategies.html)(© Copyright 2022, TradingView.).

We propose a `python` api implementation for 
>  A `strategy` ... that can send, modify and cancel buy/sell orders.

Starting with the simple strategy example:
```
//@version=4
strategy("test")
if bar_index < 100
    strategy.entry("buy_id", strategy.long, 10, when=strategy.position_size <= 0)
    strategy.order("sell_id", strategy.short, 10, when=strategy.position_size > 0)
plot(strategy.equity)
```

> The strategy places all orders that do not contradict the rules .... At each tick calculation, ...

From the above example, Pine Script [`strategy`](https://www.tradingview.com/pine-script-reference/v4/#fun_strategy) public api offer the following ["Order placement commands"](https://www.tradingview.com/pine-script-docs/en/v4/essential/Strategies.html?highlight=order%20placement%20commands#order-placement-commands):
1. `strategy.entry`, `strategy.order` to "send orders" and
3. `strategy.exit` for exit either a specific entry, or whole market position.

## Entry and Order

Given methods' signatures for order and entry are identical and we will use to design a simple `Tuple` based domain, such as:


```python
from enum import Enum

class Direction(Enum):
  LONG: bytes = b's'
  SHORT: bytes = b'l'

class OCAGroup(Enum):
  CANCEL: bytes = b'cancel'
  REDUCE: bytes = b'reduce'
  NONE: bytes = b'none'

from decimal import Decimal
from typing import ParamSpec

Qty = Decimal
Price = Decimal

P = ParamSpec('P')

from typing import AnyStr
from typing import Callable
from typing import Optional
from typing import Sequence
from typing import Tuple

Order = Tuple[
  Sequence[AnyStr], # id
  Direction, # `Direction.LONG` is for buy, `Direction.SHORT` is for sell
  Optional[Qty], # Number of contracts/shares/lots/units to trade.
  Optional[
    Tuple[
      Optional[Price], # "limit". If it is specified, the order type is either 'limit', or 'stop-limit', `None` for any other order type.
      Optional[Price], #  "stop". If it is specified, the order type is either 'stop', or 'stop-limit', `None` for any other order type.
    ]
  ],
  Optional[
    Tuple[
      Optional[AnyStr], # OCA group name
      Optional[OCAGroup], # OCA group type
    ]
  ],
  Optional[Callable[P, bool]] # Condition of the order. The order is placed if condition is 'true'. If condition is 'false', nothing happens
  # For reference only, deprecated in our design-implementation
  # Optional[AnyStr], # comment.
  # Optional[AnyStr] # alert message
]
```

```python
examples: List[Order] = [
  (
    ("some","market","buy","0"),
    Direction.LONG,
    Decimal(10),
    None,
    None,
    lambda self: self.position_size <= 0
  ),
  (
    ("some","market","sell","0"),
    Direction.SHORT,
    Decimal(10),
    None,
    None,
    lambda self: self.position_size > 0
  ),
  (
    ("some","limit","buy","0"),
    Direction.LONG,
    Decimal(10),
    (
      Decimal(0.1),
      None,
    ),
    None,
    None,
  ),
  (
    ("some","limit","sell","0"),
    Direction.LONG,
    Decimal(10),
    (
      Decimal(0.2),
      None,
    ),
    None,
    None,
  ),
]
```
>

There is a difference in behavior is found around strategy's property `pyramiding`:

> `pyramiding (const integer)` The maximum number of entries allowed in the same direction. If the value is 0, only one entry order in the same direction can be opened, and additional entry orders are rejected. The default value is 0.


In particular:

> `strategy.entry`
> It is a command to enter market position. In comparison to the function `strategy.order`, the function `strategy.entry` is affected by pyramiding and it can reverse market position correctly.

& 

> `strategy.order`
> It is a command to place order. In comparison to the function strategy.entry, the function strategy.order is not affected by pyramiding.

for most

> `strategy.exit`
> It is a command to exit either a specific entry, or whole market position. If an order with the same ID is already pending, it is possible to modify the order. If an entry order was not filled, but an exit order is generated, the exit order will wait till entry order is filled and then the exit order is placed. To deactivate an exit order, the command strategy.cancel or strategy.cancel_all should be used. If the function strategy.exit is called once, it exits a position only once. If you want to exit multiple times, the command strategy.exit should be called multiple times. If you use a stop loss and a trailing stop, their order type is 'stop', so only one of them is placed (the one that is supposed to be filled first). If all the following parameters 'profit', 'limit', 'loss', 'stop', 'trail_points', 'trail_offset' are 'NaN', the command will fail. To use market order to exit, the command strategy.close or strategy.close_all should be used.


### Pyramiding


### Mutation
where same behaviour around mutation.
> If an order with the same ID is already pending, it is possible to modify the order. If there is no order with the specified ID, a new order is placed.
> To deactivate an entry order, the command strategy.cancel or strategy.cancel_all should be used. 

### Full method signature
> If both 'limit' and 'stop' parameters are 'NaN', the order type is market order.

## Appendix

### OCA groups

OCA stands for "One-Cancells-All (OCA) groups" in Pine Script™.

- `strategy.oca.cancel`: As soon as an order from the group is filled (even partially) or cancelled, the other orders from the same group get cancelled.  ...At each tick calculation, firstly all orders with the satisfied conditions are executed and only then the orders from the group where an order was executed are cancelled.

- `strategy.oca.reduce`: This group type allows multiple orders within the group to be filled. As one of the orders within the group starts to be filled, the size of other orders is reduced by the filled contracts amount. It is very useful for the exit strategies. Once the price touches your take-profit order and it is being filled, the stop-loss is not cancelled but its amount is reduced by the filled contracts amount, thus protecting the rest of the open position.

- `strategy.oca.none`: The order is placed outside of the group (default value for the strategy.order and strategy.entry functions).

