"""
This module defines an abstract base class `List` that represents an ordered collection of elements.
It extends the `Collection` class to provide additional operations for accessing elements based on their position
and handling lists of elements.

Classes:
    - List: Abstract class for ordered collections that supports positional access.
"""

from abc import abstractmethod
from jcollections.collection import Collection

class List(Collection):
    """
    Abstract class representing an ordered collection (a list).
    Extends the Collection class to include operations specific to lists, such as positional access to elements.
    Subclasses of this class must implement all abstract methods to define specific list behaviors.
    """

    @abstractmethod
    def add(self, *args):
        """
        Adds an element or elements to the list.

        Subclasses must implement this method to define how elements are added to the list.

        This method supports two modes:

        - **Single argument**: Adds an element to the end of the list.
        - **Two arguments**: Adds an element at the specified index.
        """

        pass

    @abstractmethod
    def clear(self):
        """
        Removes all the elements from this list (optional operation).
        Subclasses must implement this method to define how to clear the list.
        """
        pass

    @abstractmethod
    def contains(self, o):
        """
        Returns True if this list contains the specified element.
        :param o: The element to check for.
        :return: True if the element is present, otherwise False.
        """
        pass

    @abstractmethod
    def containsAll(self, c):
        """
        Returns True if this list contains all the elements of the specified collection.
        :param c: The collection to check for containment.
        :return: True if all elements are present, otherwise False.
        """
        pass

    @abstractmethod
    def equals(self, o):
        """
        Compares the specified object with this list for equality.
        :param o: The object to compare with.
        :return: True if the specified object is equal to this list, otherwise False.
        """
        pass

    @abstractmethod
    def get(self, index):
        """
        Returns the element at the specified position in this list.
        :param index: The index of the element to return.
        :return: The element at the specified index.
        """
        pass

    @abstractmethod
    def hashCode(self):
        """
        Returns the hash code value for this list.
        :return: The hash code of the list.
        """
        pass

    @abstractmethod
    def indexOf(self, o):
        """
        Returns the index of the first occurrence of the specified element in this list, or -1 if the list does not contain the element.
        :param o: The element to search for.
        :return: The index of the first occurrence, or -1 if not found.
        """
        pass

    @abstractmethod
    def isEmpty(self):
        """
        Returns True if this list contains no elements.
        :return: True if the list is empty, otherwise False.
        """
        pass

    @abstractmethod
    def iterator(self):
        """
        Returns an iterator over the elements in this list in proper sequence.
        :return: An iterator for the list elements.
        """
        pass

    @abstractmethod
    def lastIndexOf(self, o):
        """
        Returns the index of the last occurrence of the specified element in this list, or -1 if the list does not contain the element.
        :param o: The element to search for.
        :return: The index of the last occurrence, or -1 if not found.
        """
        pass

    @abstractmethod
    def listIterator(self, *args):
        """
        Returns a list iterator over the elements in this list.
        :param args: Optional start index for the iterator.
        :return: A list iterator for the elements.
        """
        pass

    @abstractmethod
    def remove(self, *args):
        """
        Removes the element at the specified position in this list or a specified element.
        - No arguments: Removes the first element.
        - Single integer argument: Removes the element at the specified index.
        - Single non-integer argument: Removes the first occurrence of the specified element.
        """
        pass

    @abstractmethod
    def removeAll(self, c):
        """
        Removes from this list all of its elements that are contained in the specified collection (optional operation).
        :param c: The collection of elements to be removed.
        :return: True if the list was modified, otherwise False.
        """
        pass

    @abstractmethod
    def replaceAll(self, operator):
        """
        Replaces each element of this list with the result of applying the operator to that element.
        :param operator: A function to apply to each element.
        """
        pass

    @abstractmethod
    def retainAll(self, c):
        """
        Retains only the elements in this list that are contained in the specified collection (optional operation).
        :param c: The collection to retain elements from.
        :return: True if the list was modified, otherwise False.
        """
        pass

    @abstractmethod
    def set(self, index, element):
        """
        Replaces the element at the specified position in this list with the specified element (optional operation).
        :param index: The index of the element to replace.
        :param element: The element to replace with.
        :return: The element previously at the specified position.
        """
        pass

    @abstractmethod
    def size(self):
        """
        Returns the number of elements in this list.
        :return: The size of the list.
        """
        pass

    @abstractmethod
    def sort(self, c):
        """
        Sorts this list according to the order induced by the specified Comparator.
        :param c: The comparator to determine the order of the list.
        """
        pass

    @abstractmethod
    def spliterator(self):
        """
        Creates a Spliterator over the elements in this list.
        :return: A Spliterator for the elements.
        """
        pass

    @abstractmethod
    def subList(self, fromIndex, toIndex):
        """
        Returns a view of the portion of this list between the specified fromIndex, inclusive, and toIndex, exclusive.
        :param fromIndex: The starting index of the sublist.
        :param toIndex: The ending index of the sublist.
        :return: A sublist of the original list.
        """
        pass

    @abstractmethod
    def toArray(self, *args):
        """
        Converts the list elements into an array.
        :param args: Optional argument specifying the type of array elements.
        :return: An array containing all the elements in the list.
        """
        pass
