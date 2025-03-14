import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    """ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.
    """
    
    def __init__(self, max_size: int = 20, data_type=int) -> None:
        """Constructor to initialize the stack.
        
        Arguments: 
            max_size: int -- The maximum size of the stack. 
            data_type: type -- The data type of the stack.       
        """
        self.data_type = data_type
        self.max_size = max_size
        self.stack = Array[T](starting_sequence=[], data_type=data_type)
        self.top = -1  

    def push(self, item: T) -> None:
        """Pushes an item onto the stack."""
        if self.full:
            raise IndexError("Stack is full.")
        self.top += 1
        if self.top < len(self.stack):  
            self.stack[self.top] = item
        else:
            self.stack.append(item)  

    def pop(self) -> T:
        """Removes and returns the item from the top of the stack."""
        if self.empty:
            raise IndexError("Stack is empty.")
        item = self.stack[self.top]
        self.top -= 1
        return item

    def clear(self) -> None:
        """Clears the stack."""
        self.stack.clear()
        self.top = -1

    @property
    def peek(self) -> T:
        """Returns the item at the top without removing it."""
        if self.empty:
            raise IndexError("Stack is empty.")
        return self.stack[self.top]

    @property
    def maxsize(self) -> int:
        """Returns the maximum size of the stack."""
        return self.max_size
    
    @property
    def full(self) -> bool:
        """Returns True if the stack is full, False otherwise."""
        return self.top == self.max_size - 1

    @property
    def empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return self.top == -1
    
    def __eq__(self, other: object) -> bool:
        """Compares two stacks for equality."""
        if not isinstance(other, ArrayStack):
            return False
        if self.top != other.top:
            return False
        return all(self.stack[i] == other.stack[i] for i in range(self.top + 1))

    def __len__(self) -> int:
        """Returns the number of elements in the stack."""
        return self.top + 1
    
    def __contains__(self, item: T) -> bool:
        """Checks if an item exists in the stack."""
        return any(self.stack[i] == item for i in range(self.top + 1))

    def __str__(self) -> str:
        """Returns a string representation of the stack."""
        return str([self.stack[i] for i in range(self.top + 1)])

    def __repr__(self) -> str:
        """Returns a detailed string representation of the stack."""
        return f"ArrayStack({self.maxsize}): items: {self}"
    