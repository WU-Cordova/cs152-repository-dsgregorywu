from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue using an array. """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue with a fixed size and data type.
        
            Arguments:
                maxsize: The maximum size of the queue (excluding an extra slot for differentiation).
                data_type: The type of the elements in the queue.
        '''
        self.data_type = data_type
        self.maxsize = maxsize
        self.circularqueue = Array(starting_sequence=[data_type() for _ in range(maxsize + 1)], data_type=data_type)
        self._front = 0
        self._rear = 0

    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue.
            Raises:
                IndexError: If the queue is full.
        '''
        if self.full:
            raise IndexError("Queue is full")
        self.circularqueue[self._rear] = item
        self._rear = (self._rear + 1) % len(self.circularqueue)

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue.
            Raises:
                IndexError: If the queue is empty.
        '''
        if self.empty:
            raise IndexError("Queue is empty")
        item = self.circularqueue[self._front]
        self._front = (self._front + 1) % len(self.circularqueue)
        return item

    def clear(self) -> None:
        ''' Removes all items from the queue. '''
        self.circularqueue = Array(starting_sequence=[self.data_type() for _ in range(self.maxsize + 1)], data_type=self.data_type)
        self._front = 0
        self._rear = 0

    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it. '''
        if self.empty:
            raise IndexError("Queue is empty")
        return self.circularqueue[self._front]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise. '''
        return (self._rear + 1) % len(self.circularqueue) == self._front

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise. '''
        return self._front == self._rear

    def __eq__(self, other: object) -> bool:
        ''' Checks if two CircularQueue instances are equal. '''
        if not isinstance(other, CircularQueue):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.circularqueue[(self._front + i) % len(self.circularqueue)] != other.circularqueue[(other._front + i) % len(other.circularqueue)]:
                return False
        return True

    def __len__(self) -> int:
        ''' Returns the number of items in the queue. '''
        return (self._rear - self._front + len(self.circularqueue)) % len(self.circularqueue)

    def __str__(self) -> str:
        ''' Returns a string representation of the queue contents. '''
        items = [self.circularqueue[(self._front + i) % len(self.circularqueue)] for i in range(len(self))]
        return f"CircularQueue({items})"

    def __repr__(self) -> str:
        ''' Returns a developer-friendly string representation of the queue. '''
        return f"CircularQueue(maxsize={self.maxsize}, front={self._front}, rear={self._rear})"