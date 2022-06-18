from collections import (
    defaultdict,
)
from decimal import Decimal as PrimitiveDecimal
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)
from weakref import (
    WeakValueDictionary,
)

from . import (
    Flyweight,
)


# move from PrimitiveDecimal -> T and Decimal to Flyweight
class Decimal(PrimitiveDecimal, Flyweight):
    _memory: WeakValueDictionary[int, Flyweight] = WeakValueDictionary()
    

    # naive implementation
    def __new__(
        cls,
        value: Union[int,str,float,PrimitiveDecimal]='0',
        context: Optional[Any] = None,
    ) -> Any:
        value = super(Decimal, cls).__new__(cls, value=value, context=context)
        key = hash(value)
        cls._memory[key] = cls._memory.get(key, value)
        return cls._memory[key]

__all__ = [ 'Decimal' ]
