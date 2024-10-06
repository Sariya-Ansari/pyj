"""
AbstractQueue Module

This module defines the `AbstractQueue` class, which is an abstract base class for queue implementations.
It extends the `Collection` interface and provides abstract methods for typical queue operations such as
insertion, retrieval, and removal of elements.

The `AbstractQueue` is intended to be subclassed by concrete implementations of queues.

Classes:
    - AbstractQueue: An abstract class for queue data structures.
"""

from abc import abstractmethod
from jcollections.collection import Collection


class AbstractQueue(Collection):
    """
    AbstractQueue is an abstract class that provides a skeletal implementation of a queue.

    Concrete implementations of a queue must extend this class and implement the provided abstract methods.
    These methods define standard queue operations such as adding, removing, and retrieving elements from the queue.

    Inherits from:
        Collection: The base interface for all collection types.
    """

    @abstractmethod
    def add(self, e):
        """
        Inserts the specified element into the queue if possible, without violating capacity restrictions.

        This method may throw an exception if the insertion would exceed the queue's capacity limits.

        :param e: The element to be added to the queue.
        :type e: Any
        :returns: True if the element was successfully added.
        :raises: Exception if the queue is full or the element cannot be added.
        """
        pass

    @abstractmethod
    def element(self):
        """
        Retrieves, but does not remove, the head of this queue.

        This method throws an exception if the queue is empty.

        :returns: The head of the queue.
        :raises: Exception if the queue is empty.
        """
        pass

    @abstractmethod
    def offer(self, e):
        """
        Attempts to insert the specified element into the queue without violating capacity restrictions.

        This method is similar to `add`, but instead of throwing an exception, it returns False if the
        element cannot be added (e.g., if the queue is full).

        :param e: The element to be added to the queue.
        :type e: Any
        :returns: True if the element was successfully added, or False if the queue is full.
        """
        pass

    @abstractmethod
    def peek(self):
        """
        Retrieves, but does not remove, the head of this queue, or returns None if the queue is empty.

        :returns: The head of the queue, or None if the queue is empty.
        """
        pass

    @abstractmethod
    def poll(self):
        """
        Retrieves and removes the head of this queue, or returns None if the queue is empty.

        :returns: The head of the queue, or None if the queue is empty.
        """
        pass

    @abstractmethod
    def remove(self, o):
        """
        Retrieves and removes the head of this queue.

        This method throws an exception if the queue is empty.

        :param o: The element to be removed.
        :type o: Any
        :returns: The removed element.
        :raises: Exception if the queue is empty or the element cannot be found.
        """
        pass
