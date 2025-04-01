from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count: int = 0
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list = LinkedList(data_type=data_type)
        for item in sequence:
            linked_list.append(item)
        return linked_list

    def append(self, item: T) -> None:
        new_node = LinkedList.Node(data=item)
        if self.tail is None:  
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.count += 1

    def prepend(self, item: T) -> None:
        new_node = LinkedList.Node(data=item)
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        self.head = new_node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        if self.head is None:
            raise ValueError("List is empty")
        current = self.head
        while current and current.data != target:
            current = current.next
        if current is None:
            raise ValueError(f"Target {target} not found in the list")
        new_node = LinkedList.Node(data=item)
        if current.previous is None:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        else:
            previous_node = current.previous
            previous_node.next = new_node
            new_node.previous = previous_node
            new_node.next = current
            current.previous = new_node
        self.count += 1

    def insert_after(self, target: T, item: T) -> None:
        if self.head is None: raise ValueError("List is empty")
        current = self.head
        while current and current.data != target:
            current = current.next
        if current is None:raise ValueError(f"Target {target} not found in the list")
        new_node = LinkedList.Node(data=item)
        if current.previous is None:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        else:
            previous_node = current.previous
            previous_node.next = new_node
            new_node.previous = previous_node
            new_node.next = current
            current.previous = new_node
        self.count += 1

    def remove(self, item: T) -> None:
        if self.head is None: raise ValueError("List is empty")
        current = self.head
        while current and current.data != item:
            current = current.next
        if current is None: raise ValueError(f"{item} not found in the list")
        if current.previous is None:
            self.head = current.next
            if self.head:
                self.head.previous = None
        else:
            current.previous.next = current.next
        if current.next is None:
            self.tail = current.previous
            if self.tail:
                self.tail.next = None
        else:
            current.next.previous = current.previous
        self.count -= 1

    def remove_all(self, item: T) -> None:

        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        if self.tail is None: raise IndexError("Pop from empty list")
        data = self.tail.data
        self.tail = self.tail.previous
        if self.tail is not None:
            self.tail.next = None
        else: self.head = None
        self.count -= 1
        return data

    def pop_front(self) -> T:
        if self.tail is None: raise IndexError("Pop from empty list")
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.previous = None
        else: self.tail = None
        self.count -= 1
        return data

    @property
    def front(self) -> T:
        return self.head

    @property
    def back(self) -> T:
        return self.tail

    @property
    def empty(self) -> bool:
        if self.head: return True
        else: return False

    def __len__(self) -> int:
        return self.count
    
    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        if self.head is None: raise ValueError("List is empty")
        current = self.head
        while current and current.data != item:
            current = current.next
        if current is None: bool = False
        else: bool = True
        return bool

    def __iter__(self) -> LinkedList[T]:
        self._current = self.head  
        return self

    def __next__(self) -> T:
        if self._current is None:
            raise StopIteration  
        data = self._current.data
        self._current = self._current.next 
        return data
    
    def __reversed__(self):
        current = self.tail 
        while current:
            yield current.data
            current = current.previous
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList): return False
        if len(self) != len(other): return False
        current_self = self.head
        current_other = other.head
        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
