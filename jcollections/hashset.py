"""
The `hashset` module implements the `HashSet` class, which is a set implementation backed by a `HashMap`, ensuring unique
elements without any specific order.
"""

from jcollections.set import Set


class HashSet(Set):
    """
    HashSet implementation that does not allow duplicate elements and does not guarantee any specific order of elements.

    This class uses Python's built-in set as the internal storage. The initial capacity and load factor are ignored since
    Python sets handle these aspects automatically.

    Inherits from:
        - Set: Abstract class providing set-related operations.
    """

    def __init__(self, initial_capacity: int = 16, load_factor: float = 0.75, elements=None):
        """
        Initializes a new HashSet with an optional initial capacity, load factor, and an optional collection of elements.

        :param initial_capacity: The initial capacity for the set (ignored in Python).
        :param load_factor: The load factor for the set (ignored in Python).
        :param elements: An optional collection of elements to initialize the set with.
        """
        self._set = set()  # Internal Python set
        self._initial_capacity = initial_capacity  # Initial capacity
        self._load_factor = load_factor  # Load factor

        if elements:
            self.addAll(elements)

    def add(self, e) -> bool:
        """
        Adds the specified element to the set if it is not already present.

        :param e: The element to add.
        :return: True if the element was added, False if it was already present.
        """
        if e not in self._set:
            self._set.add(e)
            return True
        return False

    def addAll(self, c) -> bool:
        """
        Adds all elements from the specified collection to the set if they are not already present.

        :param c: The collection of elements to add.
        :return: True if any elements were added, False otherwise.
        """
        initial_size = len(self._set)
        self._set.update(c)
        return len(self._set) > initial_size

    def clear(self) -> None:
        """
        Removes all elements from the set.
        """
        self._set.clear()

    def contains(self, o) -> bool:
        """
        Checks if the set contains the specified element.

        :param o: The element to check.
        :return: True if the element is present, False otherwise.
        """
        return o in self._set

    def containsAll(self, c) -> bool:
        """
        Checks if the set contains all elements in the specified collection.

        :param c: The collection of elements to check for.
        :return: True if all elements are present, False otherwise.
        """
        return all(item in self._set for item in c)

    def equals(self, o) -> bool:
        """
        Compares this set to another object for equality.

        :param o: The object to compare with.
        :return: True if the object is a HashSet and contains the same elements, False otherwise.
        """
        if isinstance(o, HashSet):
            return self._set == o._set
        return False

    def hashCode(self) -> int:
        """
        Returns the hash code of the set.

        :return: The hash code of the set.
        """
        return hash(frozenset(self._set))

    def isEmpty(self) -> bool:
        """
        Checks if the set contains no elements.

        :return: True if the set is empty, False otherwise.
        """
        return len(self._set) == 0

    def iterator(self):
        """
        Returns an iterator over the elements in the set.

        :return: An iterator over the set's elements.
        """
        return iter(self._set)

    def remove(self, o) -> bool:
        """
        Removes the specified element from the set if it is present.

        :param o: The element to remove.
        :return: True if the element was removed, False if it was not present.
        """
        if o in self._set:
            self._set.remove(o)
            return True
        return False

    def removeAll(self, c) -> bool:
        """
        Removes all elements from the set that are also contained in the specified collection.

        :param c: The collection of elements to remove.
        :return: True if any elements were removed, False otherwise.
        """
        initial_size = len(self._set)
        self._set.difference_update(c)
        return len(self._set) < initial_size

    def retainAll(self, c) -> bool:
        """
        Retains only the elements in the set that are contained in the specified collection.

        :param c: The collection of elements to retain.
        :return: True if the set was modified, False otherwise.
        """
        initial_size = len(self._set)
        self._set.intersection_update(c)
        return len(self._set) < initial_size

    def size(self) -> int:
        """
        Returns the number of elements in the set.

        :return: The size of the set.
        """
        return len(self._set)

    def spliterator(self):
        """
        Creates a spliterator over the elements in the set (mock implementation).

        :return: An iterator over the set's elements.
        """
        return iter(self._set)

    def toArray(self):
        """
        Returns an array containing all the elements in the set.

        :return: A list of the set's elements.
        """
        return list(self._set)

    def clone(self):
        """
        Creates a shallow copy of the HashSet.

        :return: A new HashSet instance containing the same elements.
        """
        return HashSet(elements=self._set)

    def __str__(self):
        """
        Returns a string representation of the set.

        :return: The string representation of the set.
        """
        return str(self._set)

    def removeIf(self, predicate) -> bool:
        """
        Removes all elements from the set that satisfy the given predicate.

        :param predicate: A function that returns True for elements to be removed.
        :return: True if any elements were removed, False otherwise.
        """
        initial_size = len(self._set)
        self._set = {x for x in self._set if not predicate(x)}
        return len(self._set) < initial_size

    def stream(self):
        """
        Returns a sequential stream (iterator) of the set's elements.

        :return: An iterator over the set's elements.
        """
        return iter(self._set)

    def parallelStream(self):
        """
        Returns a parallel stream (iterator) of the set's elements. (Mock implementation).

        :return: An iterator over the set's elements.
        """
        return iter(self._set)

    def __iter__(self):
        """
        Returns an iterator to make the HashSet iterable.

        :return: An iterator over the set's elements.
        """
        return self.iterator()
