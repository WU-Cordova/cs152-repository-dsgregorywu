# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None:
        if not isinstance(starting_sequence, Sequence): raise ValueError("The provided data container is not a sequence type.")
        if not isinstance(data_type, type): raise ValueError("The provided data type is not a valid type.")
        self._data_type = data_type   #What type of data is being stored
        self._element_count = len(starting_sequence)    #Amount of elements in array (Logical Size)
        self._capacity = max(len(starting_sequence) * 2, 10)    #Total storage capacity of array (Physical Size)
        self._elements = np.empty(self._capacity, dtype=object)    #Actual array
        for i, item in enumerate(starting_sequence):
            if not isinstance(item, data_type):
                raise TypeError(f"Item {item} is not of type {data_type}")
            self._elements[i] = item

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...

    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, int):
            if not 0 <= index < self._element_count:
                raise IndexError("Array index out of range")
            return self._elements[index]
        else:  
            start, stop, step = index.indices(self._element_count)
            return myarray([self._elements[i] for i in range(start, stop, step)], self._data_type)
    
    def __setitem__(self, index: int, item: T) -> None:
        if not 0 <= index < self._element_count: raise IndexError("Array index out of range")
        if not isinstance(item, self._data_type): raise TypeError(f"Item {item} is not of type {self._data_type}")
        self._elements[index] = item

    def append(self, data: T) -> None:
        if not isinstance(data, self._data_type): raise TypeError(f"Item {data} is not of type {self._data_type}")
        if self._element_count >= self._capacity:
            self._capacity = self._capacity * 2
        self._elements[self._element_count] = data
        self._element_count += 1
    
    def append_front(self, data: T) -> None:
        if not isinstance(data, self._data_type): raise TypeError(f"Item {data} is not of type {self._data_type}")
        if self._element_count >= self._capacity: self._resize(self._capacity * 2)
        for i in range(self._element_count, 0, -1): self._elements[i] = self._elements[i - 1]
        self._elements[0] = data
        self._element_count += 1

    def pop(self) -> None:
        item = self._elements[self._element_count]
        myarray.__delitem__(self._element_count)
        return item
    
    def pop_front(self) -> None:
        item = self._elements[0]
        myarray.__delitem__(0)
        return item

    def __len__(self) -> int: 
        """Finds the length of the given array."""
        return self._element_count

    def __eq__(self, other: object) -> bool:
        str1 = self.__str__()
        str2 = other.__str__()
        torf = False
        if str1 == str2:
            torf = True
        return torf
    
    def __iter__(self) -> Iterator[T]:
        for i in range(self._element_count):
            yield(self._elements[i])

    def __reversed__(self) -> Iterator[T]:
        for i in range(self._element_count - 1, -1, -1):
            yield self._elements[i]

    def __delitem__(self, index: int) -> None:
        if not isinstance(index, int): raise TypeError(f"Item {index} is not of type {self._data_type}")
        self._elements[index] = None
        pointer = 0
        for i in range(self._element_count): 
            while pointer < self._element_count:
                itemstr = str(self._elements[pointer])
                torf = itemstr.isdigit()
                if torf == False:
                    self._elements[pointer] = self._elements[pointer + 1]
                    self._elements[pointer + 1] = None
                pointer += 1
        self._element_count -= 1

    def __contains__(self, item: Any) -> bool:
        """Checks if a certain item is in the sequence."""
        itemstr = str(item)
        contains = False
        for item in self._elements:
            itemstr2 = str(item)
            if itemstr == itemstr2:
                contains = True
        return contains

    def clear(self) -> None:
        self._element_count = 0
        self._capacity = 10  
        self._elements = np.empty(self._capacity, dtype=object)

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self._element_count}, Physical: {len(self._elements)}, type: {self._data_type}'
    
if __name__ == '__main__':
    myarray = Array[int](starting_sequence=[num for num in range(10)], data_type=int)
