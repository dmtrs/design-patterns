from enum import (
    Enum,
)


class Direction(Enum):
  LONG: bytes = b's'
  SHORT: bytes = b'l'

class OCAGroup(Enum):
  CANCEL: bytes = b'cancel'
  REDUCE: bytes = b'reduce'
  NONE: bytes = b'none'

#from typing import ParamSpec
from typing import (
    TypeVar,
)

ParamSpec = TypeVar('ParamSpec')

from decimal import (
    Decimal,
)

Qty = Decimal
Price = Decimal

from typing import (
    AnyStr,
    Callable,
    Optional,
    Sequence,
    Tuple,
)

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
  Optional[Callable[..., bool]] # The order is placed if condition is 'true'. If condition is 'false', nothing happens
  # For reference only, deprecated in our design-implementation
  # Optional[AnyStr], # comment.
  # Optional[AnyStr] # alert message
]
