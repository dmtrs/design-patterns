from abc import (
    ABCMeta,
)
from collections.abc import (
    Hashable,
)
from typing import (
    Dict,
)


# not move
class Flyweight(Hashable, metaclass=ABCMeta): ...

from . import (
    decimal,
    fractions,
    numbers,
)

__all__ = [
    'decimal',
    'fractions',
    'numbers',
    'Flyweight',
]
