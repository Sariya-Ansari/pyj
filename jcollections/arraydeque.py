"""
ArrayDeque Module

This module defines the `ArrayDeque` class, a resizable-array implementation of a deque.
It provides methods for adding, removing, and accessing elements in a double-ended queue (deque).

Classes:
    - ArrayDeque: A class that implements a double-ended queue using a resizable array.

"""

from jcollections.collection import Collection


class ArrayDeque(Collection):
    """
    ArrayDeque is a resizable-array implementation of the Deque (double-ended queue) interface.

    It supports element insertion and removal from both ends of the queue.
    The class offers operations for efficiently adding elements at both the front and back,
    while also allowing for element removal and access.

    Inherits from:
        Collection: The base interface for all collection types.

    Attributes:
        _deque (list): The underlying list that stores elements.
        _capacity (int, optional): The initial capacity of the deque if specified.
    """

    def __init__(self, initial=None):
        """
        Constructs an empty deque or deque with an initial collection or initial capacity.

        :param initial: Can be None (default), a Collection, or an integer (capacity).
        :type initial: Optional[Collection or int]
        :raises TypeError: If the initial argument is not None, Collection, or int.
        """
        self._deque = []

        if initial is None:
            self._deque = []
        elif isinstance(initial, Collection) or isinstance(initial, list):
            for item in initial:
                self.add(item)
        elif isinstance(initial, int):
            self._capacity = initial
            self._deque = [None] * initial
        else:
            raise TypeError("Invalid argument type. Must be None, Collection, or an integer.")

    def __iter__(self):
        """
        Returns an iterator over the elements in the deque in proper sequence.

        :returns: An iterator over the deque elements.
        :rtype: Iterator
        """
        return iter(self._deque)

    def iterator(self):
        """
        Returns an iterator over the elements in the deque.

        :returns: An iterator over the deque elements.
        :rtype: Iterator
        """
        return iter(self._deque)

    def add(self, e):
        """
        Inserts the specified element at the end of the deque (tail).

        :param e: The element to be added.
        :type e: Any
        :returns: True if the element was successfully added.
        :rtype: bool
        """
        self._deque.append(e)
        return True

    def addFirst(self, e):
        """
        Inserts the specified element at the front of the deque.

        :param e: The element to be added at the front.
        :type e: Any
        """
        self._deque.insert(0, e)

    def addLast(self, e):
        """
        Inserts the specified element at the end of the deque.

        :param e: The element to be added at the end.
        :type e: Any
        """
        self._deque.append(e)

    def addAll(self, collection):
        """
        Adds all elements from another collection to the deque.

        :param collection: The collection of elements to be added.
        :type collection: Collection
        :returns: True if all elements were added.
        :rtype: bool
        """
        for item in collection:
            self.add(item)
        return True

    def contains(self, o):
        """
        Returns True if the deque contains the specified element.

        :param o: The element to check for.
        :type o: Any
        :returns: True if the element is present, False otherwise.
        :rtype: bool
        """
        return o in self._deque

    def descendingIterator(self):
        """
        Returns an iterator over the elements in reverse order.

        :returns: An iterator over the deque elements in reverse order.
        :rtype: Iterator
        """
        return iter(self._deque[::-1])

    def element(self):
        """
        Retrieves, but does not remove, the first element of the deque.

        :returns: The first element of the deque.
        :rtype: Any
        :raises IndexError: If the deque is empty.
        """
        return self.getFirst()

    def getFirst(self):
        """
        Retrieves, but does not remove, the first element.

        :returns: The first element in the deque.
        :rtype: Any
        :raises IndexError: If the deque is empty.
        """
        if not self._deque:
            raise IndexError("Deque is empty")
        return self._deque[0]

    def getLast(self):
        """
        Retrieves, but does not remove, the last element.

        :returns: The last element in the deque.
        :rtype: Any
        :raises IndexError: If the deque is empty.
        """
        if not self._deque:
            raise IndexError("Deque is empty")
        return self._deque[-1]

    def offer(self, e):
        """
        Inserts the element at the tail if possible.

        :param e: The element to be added.
        :type e: Any
        :returns: True if the element was added.
        :rtype: bool
        """
        return self.addLast(e)

    def offerFirst(self, e):
        """
        Inserts the element at the front of the deque.

        :param e: The element to be added at the front.
        :type e: Any
        :returns: True if the element was added.
        :rtype: bool
        """
        return self.addFirst(e)

    def offerLast(self, e):
        """
        Inserts the element at the end of the deque.

        :param e: The element to be added at the end.
        :type e: Any
        :returns: True if the element was added.
        :rtype: bool
        """
        return self.addLast(e)

    def peek(self):
        """
        Retrieves, but does not remove, the first element of the deque.

        :returns: The first element, or None if the deque is empty.
        :rtype: Any
        """
        return self.peekFirst()

    def peekFirst(self):
        """
        Retrieves, but does not remove, the first element.

        :returns: The first element, or None if the deque is empty.
        :rtype: Any
        """
        return self._deque[0] if self._deque else None

    def peekLast(self):
        """
        Retrieves, but does not remove, the last element.

        :returns: The last element, or None if the deque is empty.
        :rtype: Any
        """
        return self._deque[-1] if self._deque else None

    def poll(self):
        """
        Retrieves and removes the first element.

        :returns: The first element, or None if the deque is empty.
        :rtype: Any
        """
        return self.pollFirst()

    def pollFirst(self):
        """
        Retrieves and removes the first element.

        :returns: The first element, or None if the deque is empty.
        :rtype: Any
        """
        return self._deque.pop(0) if self._deque else None

    def pollLast(self):
        """
        Retrieves and removes the last element.

        :returns: The last element, or None if the deque is empty.
        :rtype: Any
        """
        return self._deque.pop() if self._deque else None

    def pop(self):
        """
        Pops an element from the stack (first element).

        :returns: The first element after removing it.
        :rtype: Any
        """
        return self.pollFirst()

    def push(self, e):
        """
        Pushes an element onto the stack (head of the deque).

        :param e: The element to be pushed.
        :type e: Any
        """
        self.addFirst(e)

    def remove(self, o=None):
        """
        Retrieves and removes the first element, or removes a specific element.

        :param o: Optional. The element to remove.
        :type o: Any
        :returns: The removed element, or True if a specific element was removed.
        :rtype: Any or bool
        :raises IndexError: If the deque is empty when removing the first element.
        """
        if o is None:
            return self.pollFirst()
        else:
            try:
                self._deque.remove(o)
                return True
            except ValueError:
                return False

    def removeFirst(self):
        """
        Retrieves and removes the first element.

        :returns: The first element, or None if the deque is empty.
        :rtype: Any
        """
        return self.pollFirst()

    def removeLast(self):
        """
        Retrieves and removes the last element.

        :returns: The last element, or None if the deque is empty.
        :rtype: Any
        """
        return self.pollLast()

    def removeFirstOccurrence(self, o):
        """
        Removes the first occurrence of the specified element.

        :param o: The element to be removed.
        :type o: Any
        :returns: True if the element was found and removed, False otherwise.
        :rtype: bool
        """
        return self.remove(o)

    def removeLastOccurrence(self, o):
        """
        Removes the last occurrence of the specified element.

        :param o: The element to be removed.
        :type o: Any
        :returns: True if the element was found and removed, False otherwise.
        :rtype: bool
        """
        if o in self._deque:
            index = len(self._deque) - 1 - self._deque[::-1].index(o)
            del self._deque[index]
            return True
        return False

    def size(self):
        """
        Returns the number of elements in the deque.

        :returns: The number of elements.
        :rtype: int
        """
        return len(self._deque)

    def clear(self):
        """
        Removes all elements from the deque.
        """
        self._deque.clear()

    def containsAll(self, c):
        """
        Returns True if the deque contains all elements from the specified collection.

        :param c: The collection of elements to check.
        :type c: Collection
        :returns: True if all elements are present, False otherwise.
        :rtype: bool
        """
        return all(item in self._deque for item in c)

    def equals(self, o):
        """
        Compares this deque with another for equality.

        :param o: The other deque to compare with.
        :type o: ArrayDeque
        :returns: True if the two deques are equal, False otherwise.
        :rtype: bool
        """
        if not isinstance(o, ArrayDeque):
            return False
        return self._deque == o._deque

    def hashCode(self):
        """
        Returns a hash code for the deque.

        :returns: The hash code of the deque.
        :rtype: int
        """
        return hash(tuple(self._deque))

    def isEmpty(self):
        """
        Returns True if the deque is empty.

        :returns: True if the deque is empty, False otherwise.
        :rtype: bool
        """
        return len(self._deque) == 0

    def removeAll(self, c):
        """
        Removes all elements in the deque that are also contained in the specified collection.

        :param c: The collection of elements to be removed.
        :type c: Collection
        :returns: True if any elements were removed, False otherwise.
        :rtype: bool
        """
        modified = False
        for item in c:
            while item in self._deque:
                self._deque.remove(item)
                modified = True
        return modified

    def removeIf(self, predicate):
        """
        Removes all elements of the deque that satisfy the given predicate.

        :param predicate: A function that returns True for elements to be removed.
        :type predicate: Callable
        :returns: True if any elements were removed, False otherwise.
        :rtype: bool
        """
        original_size = len(self._deque)
        self._deque = [item for item in self._deque if not predicate(item)]
        return len(self._deque) != original_size

    def retainAll(self, c):
        """
        Retains only the elements in the deque that are also in the specified collection.

        :param c: The collection of elements to retain.
        :type c: Collection
        :returns: True if any elements were retained, False otherwise.
        :rtype: bool
        """
        original_size = len(self._deque)
        self._deque = [item for item in self._deque if item in c]
        return len(self._deque) != original_size

    def spliterator(self):
        """
        Creates a spliterator over the elements in the deque.

        :returns: A spliterator for the deque.
        :rtype: Iterator
        """
        # Placeholder for spliterator functionality
        pass

    def stream(self):
        """
        Returns a sequential stream with this deque as its source.

        :returns: A stream over the deque elements.
        :rtype: Iterator
        """
        # Placeholder for stream functionality
        pass

    def parallelStream(self):
        """
        Returns a possibly parallel stream with this deque as its source.

        :returns: A parallel stream over the deque elements.
        :rtype: Iterator
        """
        # Placeholder for parallel stream functionality
        pass

    def toArray(self, *args):
        """
        Converts the deque to an array.

        :returns: A list representing the elements in the deque.
        :rtype: list
        """
        return list(self._deque)
