import ctypes
from typing import (
    Any,
    Union,
)
from weakref import (
    WeakValueDictionary,
)

from . import (
    Flyweight,
)


class c_ulong(Flyweight):
    _memory: WeakValueDictionary[int, Flyweight] = WeakValueDictionary()

    def __new__(cls, value: int) -> Any:
        self = super(c_ulong, cls).__new__(cls)
        self._c = ctypes.c_ulong(value)
        
        key = hash(self)
        cls._memory[key] = cls._memory.get(key, self)
        return cls._memory[key]

    @property
    def value(self) -> int:
        return int(self._c.value)

    def __hash__(self) -> int:
        return hash(self.value)


class c_uint(Flyweight):
    _memory: WeakValueDictionary[int, Flyweight] = WeakValueDictionary()

    def __new__(cls, value:int) -> Any:
        self = super(c_uint, cls).__new__(cls)
        self._c = ctypes.c_uint(value)
        
        key = hash(self)
        cls._memory[key] = cls._memory.get(key, self)
        return cls._memory[key]

    @property
    def value(self) -> int:
        return int(self._c.value)

    def __hash__(self) -> int:
        return hash(self.value)


__all__ = [
    'c_ulong',
    'c_uint',
]
