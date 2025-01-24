from typing import Iterable, Optional
from datastructures.ibag import IBag, T
import random


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self._contents = []
        self._count = {}

    def add(self, item: T) -> None:
        if item == None:
            raise TypeError("object none type.")
        elif item not in self._contents():
            self._contents.append(item)
            self._count[item] = 1
        elif item in self._contents():
            self._count(item) += 1


    def remove(self, item: T) -> None:
        raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> int:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")