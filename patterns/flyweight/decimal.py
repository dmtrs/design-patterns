from collections import (
    defaultdict,
)
from decimal import Decimal as PrimitiveDecimal
from typing import (
    Dict,
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
    def __new__(cls, *args, **kwargs) -> Flyweight:
        value = super(Decimal, cls).__new__(cls,*args, **kwargs)
        key = hash(value)
        cls._memory[key] = cls._memory.get(key, value)
        return cls._memory[key]

__all__ = [ 'Decimal' ]