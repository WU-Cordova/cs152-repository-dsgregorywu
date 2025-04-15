import os
from datastructures.istack import IStack
from typing import Generic

from datastructures.linkedlist import LinkedList, T

class ListStack(Generic[T], IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """
    

    def __init__(self, data_type:object) -> None:
        """
        Initializes the ListStack.

        Args:
            data_type (type): The type of data the stack will hold.

        """
        self.stack = LinkedList(data_type=data_type)
        self.type = data_type

    def push(self, item: T):
        """
        Pushes an item onto the stack.

        Args:
            item (T): The item to push onto the stack.
        
        Raises:
            TypeError: If the item is not of the correct type.

        """
        if not isinstance(item, self.type): raise TypeError("Item is not of correct type.")
        self.stack.prepend(item)

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if len(self.stack) == 0: raise IndexError("Stack is empty.")
        popped = self.stack.pop_front()
        return popped

    def peek(self) -> T:
        """
        Returns the top item from the stack without removing it.

        Returns:
            T: The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if len(self.stack) == 0: raise IndexError("Stack is empty.")
        item = self.stack.front
        return item

    @property
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        bool1 = False
        if len(self.stack) == 0: bool1 = True
        return bool1

    def clear(self):
        """
        Clears all items from the stack.
        """
        self.stack.clear()

    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the stack.

        Args:
            item (T): The item to check for.

        Returns:
            bool: True if the item exists in the stack, False otherwise.

        """
        return item in self.stack

    def __eq__(self, other) -> bool:
        """
        Compares two stacks for equality.

        Args:
            other (ListStack): The stack to compare with.

        Returns:
            bool: True if the stacks are equal, False otherwise.

        """
        if not isinstance(other, ListStack): raise TypeError("Other is not a ListStack.")
        return self.stack == other.stack

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.stack)

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.

        Returns:
            str: A string representation of the stack.
        """
        items = []
        current = self.stack.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the stack.

        Returns:
            str: A detailed string representation of the stack.

        """
        items = []
        current = self.stack.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"ListStack({' <-> '.join(items)}) Count: {self.stack.count}"
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
