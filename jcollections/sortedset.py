"""
This module defines an abstract base class `SortedSet`, which represents a sorted set of unique elements.

Classes:
    - SortedSet: Abstract base class for a set that maintains its elements in a sorted order.

Methods:
    - comparator: Returns the comparator used to order the elements, or None if natural ordering is used.
    - first: Returns the first (lowest) element currently in the set.
    - last: Returns the last (highest) element currently in the set.
    - headSet: Returns a view of the set with elements strictly less than a specified element.
    - subSet: Returns a view of the set with elements between two specified elements.
    - tailSet: Returns a view of the set with elements greater than or equal to a specified element.
    - spliterator: Creates a Spliterator over the elements in the set (optional implementation).
"""

from abc import ABC, abstractmethod
from jcollections.set import Set


class SortedSet(Set, ABC):
    """
    Abstract base class representing a sorted set of unique elements.

    Provides methods to access and manipulate elements in a set while maintaining sorted order.

    Methods:
        comparator: Returns the comparator used to order the elements, or None if natural ordering is used.
        first: Returns the first (lowest) element currently in the set.
        last: Returns the last (highest) element currently in the set.
        headSet: Returns a view of the set with elements strictly less than a specified element.
        subSet: Returns a view of the set with elements between two specified elements.
        tailSet: Returns a view of the set with elements greater than or equal to a specified element.
        spliterator: Creates a Spliterator over the elements in the set (optional implementation).
    """

    @abstractmethod
    def comparator(self):
        """
        Returns the comparator used to order the elements in this set, or None
        if this set uses the natural ordering of its elements.

        :return: A comparator function used to order the elements, or None if natural ordering is used.
        """
        pass

    @abstractmethod
    def first(self):
        """
        Returns the first (lowest) element currently in this set.

        :return: The first (lowest) element in the set.
        :raises: ValueError if the set is empty.
        """
        pass

    @abstractmethod
    def last(self):
        """
        Returns the last (highest) element currently in this set.

        :return: The last (highest) element in the set.
        :raises: ValueError if the set is empty.
        """
        pass

    @abstractmethod
    def headSet(self, toElement):
        """
        Returns a view of the portion of this set whose elements are strictly less than `toElement`.

        :param toElement: The high endpoint (exclusive) of the subset.
        :return: A view of the portion of this set whose elements are strictly less than `toElement`.
        """
        pass

    @abstractmethod
    def subSet(self, fromElement, toElement):
        """
        Returns a view of the portion of this set whose elements range from `fromElement` (inclusive) to `toElement` (exclusive).

        :param fromElement: The low endpoint (inclusive) of the subset.
        :param toElement: The high endpoint (exclusive) of the subset.
        :return: A view of the portion of this set whose elements range from `fromElement` to `toElement`.
        """
        pass

    @abstractmethod
    def tailSet(self, fromElement):
        """
        Returns a view of the portion of this set whose elements are greater than or equal to `fromElement`.

        :param fromElement: The low endpoint (inclusive) of the subset.
        :return: A view of the portion of this set whose elements are greater than or equal to `fromElement`.
        """
        pass

    def spliterator(self):
        """
        Creates a Spliterator over the elements in this sorted set (optional implementation).

        A Spliterator is used to traverse and partition elements of the set. This method is optional and can be
        implemented to provide a custom traversal mechanism.

        :return: A Spliterator over the elements in this set.
        """
        pass
