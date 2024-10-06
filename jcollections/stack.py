"""
This module defines the `Stack` class, which is a last-in-first-out (LIFO) stack of elements.
The `Stack` class inherits from the `Vector` class and provides additional methods for stack operations such as
push, pop, peek, and search.

Classes:
    - Stack: A LIFO stack that extends the `Vector` class.

Methods:
    - empty: Checks if the stack is empty.
    - peek: Returns the object at the top of the stack without removing it.
    - pop: Removes and returns the object at the top of the stack.
    - push: Pushes an item onto the top of the stack.
    - search: Searches for an object in the stack and returns its 1-based position from the top.
"""

from jcollections.vector import Vector

class Stack(Vector):
    """
    A LIFO (Last-In-First-Out) stack of elements that extends the Vector class.
    Provides methods for typical stack operations such as pushing, popping, and peeking elements.

    Inherits from:
        - Vector: The stack is internally implemented as a dynamically resizable array.
    """

    def __init__(self):
        """
        Initializes an empty stack by calling the constructor of the parent `Vector` class.
        """
        super().__init__()

    def empty(self):
        """
        Checks if the stack is empty.

        :return: True if the stack contains no elements, False otherwise.
        """
        return self.elementCount == 0

    def peek(self):
        """
        Returns the object at the top of the stack without removing it.

        :return: The object at the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.empty():
            raise IndexError("peek from empty stack")
        return self.elementData[self.elementCount - 1]

    def pop(self):
        """
        Removes and returns the object at the top of the stack.

        :return: The object that was at the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.empty():
            raise IndexError("pop from empty stack")
        element = self.elementData[self.elementCount - 1]
        self.removeElementAt(self.elementCount - 1)
        return element

    def push(self, item):
        """
        Pushes the given item onto the top of the stack.

        :param item: The item to push onto the stack.
        :return: The pushed item.
        """
        self.addElement(item)
        return item

    def search(self, o):
        """
        Searches for the given object in the stack and returns its 1-based position from the top.
        The top element is considered position 1.

        :param o: The object to search for in the stack.
        :return: The 1-based position of the object from the top of the stack, or -1 if the object is not found.
        """
        try:
            index = self.lastIndexOf(o)
            if index == -1:
                return -1  # Element not found
            return self.elementCount - index
        except ValueError:
            return -1
