from abc import (
    ABCMeta
)
from collections.abc import (
    Hashable
)
from typing import (
    Dict
)


# TODO: look into https://docs.python.org/3/library/weakref.html
class Flyweight(Hashable, metaclass=ABCMeta): ...

__all__ = [
    'Flyweight',
]