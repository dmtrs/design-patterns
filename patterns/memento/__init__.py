from abc import (
    ABCMeta,
    abstractmethod
)
from collections import (
    deque
)
from typing import (
    Deque,
    Iterable,
    Optional,
    Tuple
)


class Memento:
    class State(ABCMeta):
        ...

    def __init__(self, state: State):
        self._state = state

    @property
    def state(self) -> State:
        return self._state


class Originator(metaclass=ABCMeta):
    @property
    @abstractmethod
    def _state(self) -> Memento.State:
        "returns state"

    @_state.setter
    @abstractmethod
    def _state(self, state: Memento.State):
        "sets state"

    @property
    def memento(self) -> Memento:
        return Memento(self._state)

    @memento.setter
    def memento(self, m: Memento):
        self._state = m.state


class Caretaker():
    def __init__(self, origin: Originator):
        self.origin = origin

class HistoricCaretaker(Caretaker):
    def __init__(self, origin: Originator, history: Optional[Iterable[Memento]] = None):
        super().__init__(origin)
        self._history: Deque[Memento] = deque()
        for m in (history or []):
            self._append(m)

        self.store()

    def _append(self, memento: Memento) -> Memento:
        self._history.append(memento)
        return self._history[-1]

    def restore(self, memento: Memento) -> Memento:
        self.origin.memento = memento
        return self.store()

    def store(self) -> Memento:
        return self._append(self.origin.memento)

    def undo(self) -> Optional[Memento]:
        if len(self._history) == 1:
            return None

        # raise IndexError as should guard 1 item
        _pop = self._history.pop()
        self.origin.memento = self._history[-1]
        return _pop

__all__ = [
    'HistoricCaretaker',
    'Memento', 
    'Originator',
]
