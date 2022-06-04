import uuid
from typing import Dict        
from dataclasses import dataclass

from patterns import memento


class TestMemento:
    @dataclass
    class DummyCounter(memento.Originator):
        id: uuid.UUID
        c: int = 0

        @property
        def _state(self) -> Dict[str,str]:
            return {'id':str(self.id), 'c': self.c}
        
        @_state.setter
        def _state(self, state: Dict[str,str]):
            self.c = state.get('c', state['c'])

    def test_init(self) -> None:
        # arrange
        counter = TestMemento.DummyCounter(uuid.uuid4())
        taker = memento.HistoricCaretaker(counter)

        # assert / act
        assert counter.c == 0

        counter.c += 1
        assert counter.c == taker.store().state['c'] == 1
        
        assert taker.undo().state['c'] == 1
        assert counter.c == 0
        
        assert not taker.undo()

    def test_init_history(self) -> None:
        # arrange
        counter = TestMemento.DummyCounter(uuid.uuid4(), 101)
        taker = memento.HistoricCaretaker(counter, [ memento.Memento({'c':100}) ])

        # assert / act
        assert counter.c == 101
        assert taker.undo().state['c'] == 101
        assert counter.c == 100

    def test_restore(self) -> None:
        # arrange
        counter = TestMemento.DummyCounter(uuid.uuid4(), 0)
        taker = memento.HistoricCaretaker(counter)

        # assert / act
        assert taker.restore(memento.Memento({'c': 100})).state['c'] == counter.c == 100
        assert taker.undo().state['c'] == 100
        assert counter.c == 0
        
        assert not taker.undo()
