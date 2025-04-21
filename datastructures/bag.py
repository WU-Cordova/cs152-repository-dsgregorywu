from typing import Iterable, Optional
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self._contents = []
        self._count = {}

    def add(self, item: T) -> None:
        if item != None:
            if item not in self._count:
                self._contents.append(item)
                self._count[item] = int(1)
            else: self._count[item] += 1
        else: raise TypeError("object none type.")


    def remove(self, item: T) -> None:
        if item != None:
            if item not in self._count:
                raise ValueError("item not in bag")
            else:
                self._contents.remove(item)
                self._count[item] -= 1
                if self._count[item] == 0:
                    self._count.pop(item)
        else: raise ValueError("object type none")


    def count(self, item: T) -> int:
        if item != None:
            if item in self._count:
                return self._count[item]
            else: return 0
        else: raise TypeError("object type none")

    def __len__(self) -> int:
        itemsinbag = int(0)
        for item in self._count.keys():
            itemcount = int(self._count[item])
            itemsinbag += itemcount
        return itemsinbag


    def distinct_items(self) -> int:
        distitems = set()
        for item in self._count.keys():
            distitems.add(item)
        return distitems

    def __contains__(self, item) -> bool:
        if item == None:
            raise TypeError("object none type")
        if item in self._contents:
            return True
        else: return False

    def clear(self) -> None:
        self._contents = []
        self._count = {}

    def print_contents(self):
        for item in self._contents:
            print(item)
