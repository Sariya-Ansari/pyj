"""
The `collection` module defines the `Collection` abstract class, which serves as the foundation for various collection types.
It includes common methods such as `add`, `remove`, and `contains`.
"""

from abc import abstractmethod
from jcollections.Iterable import Iterable


class Collection(Iterable):
    """
    Abstract class representing a general collection of elements.
    Extends the Iterable class to allow for iteration over the collection.
    Subclasses must implement all abstract methods to define specific collection behaviors.
    """

    @abstractmethod
    def add(self, *args):
        """
        Adds an element or elements to the collection.

        :param args: Element(s) to add to the collection. Subclasses must implement
        this method to define how elements are added to the collection.
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Removes all the elements from this collection (optional operation).

        Subclasses must implement this method to define how to clear the collection.
        """
        pass

    @abstractmethod
    def contains(self, o):
        """
        Returns True if this collection contains the specified element.

        :param o: The element to check for in the collection.
        :return: True if the element is present, otherwise False.
        """
        pass

    @abstractmethod
    def containsAll(self, c):
        """
        Returns True if this collection contains all the elements in the specified collection.

        :param c: The collection to check for containment.
        :return: True if all elements from the specified collection are present, otherwise False.
        """
        pass

    @abstractmethod
    def equals(self, o):
        """
        Compares the specified object with this collection for equality.

        :param o: The object to compare with.
        :return: True if the specified object is equal to this collection, otherwise False.
        """
        pass

    @abstractmethod
    def hashCode(self):
        """
        Returns the hash code value for this collection.

        :return: The hash code value.
        """
        pass

    @abstractmethod
    def isEmpty(self):
        """
        Returns True if this collection contains no elements.

        :return: True if the collection is empty, otherwise False.
        """
        pass

    @abstractmethod
    def iterator(self):
        """
        Returns an iterator over the elements in this collection.

        :return: An iterator for iterating over the collection's elements.
        """
        pass

    @abstractmethod
    def parallelStream(self):
        """
        Returns a possibly parallel Stream with this collection as its source.

        :return: A possibly parallel Stream for processing the collection.
        """
        pass

    @abstractmethod
    def remove(self, o):
        """
        Removes a single instance of the specified element from this collection, if present.

        :param o: The element to be removed.
        :return: True if the element was removed, otherwise False.
        """
        pass

    @abstractmethod
    def removeAll(self, c):
        """
        Removes all of this collection's elements that are also contained in the specified collection (optional operation).

        :param c: The collection of elements to be removed from this collection.
        :return: True if the collection changed as a result of the operation, otherwise False.
        """
        pass

    @abstractmethod
    def removeIf(self, predicate):
        """
        Removes all the elements of this collection that satisfy the given predicate.

        :param predicate: A function that returns True for elements to be removed.
        :return: True if any elements were removed, otherwise False.
        """
        pass

    @abstractmethod
    def retainAll(self, c):
        """
        Retains only the elements in this collection that are contained in the specified collection (optional operation).

        :param c: The collection of elements to retain in this collection.
        :return: True if the collection changed as a result of the operation, otherwise False.
        """
        pass

    @abstractmethod
    def size(self):
        """
        Returns the number of elements in this collection.

        :return: The number of elements in the collection.
        """
        pass

    @abstractmethod
    def spliterator(self):
        """
        Creates a Spliterator over the elements in this collection.

        :return: A Spliterator for traversing the elements of the collection.
        """
        pass

    @abstractmethod
    def stream(self):
        """
        Returns a sequential Stream with this collection as its source.

        :return: A sequential Stream for processing the collection's elements.
        """
        pass

    @abstractmethod
    def toArray(self, *args):
        """
        Converts the elements of the collection into an array.

        :param args: Optional argument specifying the type of array elements.
        :return: An array containing all elements in the collection.
        """
        pass
