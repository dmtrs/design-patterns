from decimal import Decimal as PrimitiveDecimal

from collections import defaultdict
from typing import Dict

from . import Flyweight

# TODO: look into https://docs.python.org/3/library/weakref.html

# move from PrimitiveDecimal -> T and Decimal to Flyweight
class Decimal(PrimitiveDecimal, Flyweight):
    _memory: Dict[int, Flyweight] = defaultdict(lambda:{})

    # naive implementation
    def __new__(cls, *args, **kwargs) -> Flyweight:
        value = super(Decimal, cls).__new__(cls,*args, **kwargs)
        key = hash(value)
        if key not in cls._memory:
            cls._memory[key] = value
        else:
            del value
        return cls._memory[key]

__all__ = [ 'Decimal' ]