from collections import (
    defaultdict,
)
from decimal import Context as DecimalContext
from decimal import Decimal as PrimitiveDecimal
from typing import (
    Any,
    Dict,
    Optional,
    Tuple,
    TypeVar,
    Union,
)
from weakref import (
    WeakValueDictionary,
)

from . import (
    Flyweight,
)

DecimalValue = Union[
    int,
    str,
    float,
    PrimitiveDecimal,
    Tuple[int, Tuple[int], int],
]

# move from PrimitiveDecimal -> T and Decimal to Flyweight
class Decimal(PrimitiveDecimal, Flyweight):
    _memory: WeakValueDictionary[int, Flyweight] = WeakValueDictionary()
    

    # naive implementation
    def __new__(
        cls,
        value: DecimalValue='0',
        context: Optional[DecimalContext] = None,
    ) -> Any:
        value = super(Decimal, cls).__new__(
            cls,
            value=value,
            context=context
        )
        key = hash(value)
        cls._memory[key] = cls._memory.get(key, value)
        return cls._memory[key]

__all__ = [ 'Decimal' ]
