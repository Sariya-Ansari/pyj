"""
This module defines a `Queue` class that provides a basic queue implementation using either an `ArrayList` or a `LinkedList` for internal storage.

Classes:
    - Queue: A class that provides queue operations such as add, remove, and peek, using either an ArrayList or a LinkedList.
"""

from jcollections.arraylist import ArrayList
from jcollections.linkedlist import LinkedList


class Queue:
    """
    A queue implementation that can be backed by either an ArrayList or a LinkedList.

    The choice of list type affects the underlying behavior of certain operations.
    ArrayList is generally faster for indexed access, while LinkedList is better suited for insertion and deletion at the head or tail.
    """

    def __init__(self, list_type):
        """
        Initializes a queue with the specified list type (ArrayList or LinkedList).

        :param list_type: The list type (ArrayList or LinkedList) to use for internal storage.
        """
        self.list = list_type

    def addLast(self, element):
        """
        Adds the given element to the end of the queue.

        Depending on the underlying list type:
        - ArrayList: Uses `add` to append the element.
        - LinkedList: Uses `addLast` to append the element at the end.

        :param element: The element to add to the queue.
        """
        if isinstance(self.list, ArrayList):
            self.list.add(element)  # For ArrayList, use add (appends at the end)
        elif isinstance(self.list, LinkedList):
            self.list.addLast(element)  # For LinkedList, use addLast

    def removeFirst(self):
        """
        Removes and returns the first element of the queue.

        Depending on the underlying list type:
        - ArrayList: Removes the element at index 0.
        - LinkedList: Uses `removeFirst` to remove the first element.

        Raises IndexError if the queue is empty.

        :return: The first element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if isinstance(self.list, ArrayList):
            if not self.list.isEmpty():
                return self.list.remove(0)  # For ArrayList, remove first element
            else:
                raise IndexError("Queue is empty")
        elif isinstance(self.list, LinkedList):
            return self.list.removeFirst()  # For LinkedList, directly removeFirst

    def peek(self):
        """
        Retrieves, but does not remove, the first element of the queue.

        Depending on the underlying list type:
        - ArrayList: Retrieves the element at index 0.
        - LinkedList: Uses `peekFirst` to retrieve the first element.

        Returns None if the queue is empty.

        :return: The first element of the queue, or None if the queue is empty.
        """
        if isinstance(self.list, ArrayList):
            if not self.list.isEmpty():
                return self.list.get(0)  # For ArrayList, get the first element
            return None
        elif isinstance(self.list, LinkedList):
            return self.list.peekFirst()  # For LinkedList, peekFirst is available

    def poll(self):
        """
        Removes and returns the first element of the queue.

        Depending on the underlying list type:
        - ArrayList: Removes and returns the element at index 0.
        - LinkedList: Uses `pollFirst` to remove and return the first element.

        Returns None if the queue is empty.

        :return: The first element of the queue, or None if the queue is empty.
        """
        if isinstance(self.list, ArrayList):
            if not self.list.isEmpty():
                return self.removeFirst()  # For ArrayList, remove and return the first element
            return None
        elif isinstance(self.list, LinkedList):
            return self.list.pollFirst()  # For LinkedList, pollFirst is available

    def element(self):
        """
        Retrieves but does not remove the first element of the queue.

        Depending on the underlying list type:
        - ArrayList: Retrieves the element at index 0 and raises IndexError if the queue is empty.
        - LinkedList: Uses `peekFirst` and raises IndexError if the queue is empty.

        :return: The first element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if isinstance(self.list, ArrayList):
            if not self.list.isEmpty():
                return self.list.get(0)
            else:
                raise IndexError("No Such Element")  # Different from peek (raises exception if empty)
        elif isinstance(self.list, LinkedList):
            result = self.list.peekFirst()
            if result is None:
                raise IndexError("No Such Element")
            return result

    def offer(self, element):
        """
        Inserts the given element into the queue.

        Since capacity restrictions are not handled, this method behaves the same as `addLast`.

        :param element: The element to insert into the queue.
        :return: True to indicate successful insertion.
        """
        self.addLast(element)
        return True

    def getList(self):
        """
        Returns the internal list instance used by the queue.

        :return: The internal list instance (ArrayList or LinkedList).
        """
        return self.list
