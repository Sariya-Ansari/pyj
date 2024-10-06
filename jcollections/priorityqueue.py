"""
This module defines a `PriorityQueue` class, which provides a priority-based ordering of elements
using a heap. The class supports common queue operations such as adding, peeking, polling, and more.

Classes:
    - PriorityQueue: A collection that stores elements in priority order, optionally using a comparator.
"""

from heapq import heappush, heappop, heapify
from jcollections.collection import Collection
from jcollections.queue import Queue

class PriorityQueue(Collection, Queue):
    """
    A priority queue implementation using a binary heap. This class allows elements to be stored
    and retrieved based on their priority. An optional comparator can be provided for custom ordering.

    Attributes:
        _heap (list): Internal heap structure to store elements.
        comparator (Callable, optional): A function to compare elements for priority ordering.
    """

    def __init__(self, initial=None, comparator=None, initial_capacity=11):
        """
        Initializes a PriorityQueue with optional initial elements, a comparator, and an initial capacity.

        :param initial: Collection or list of initial elements.
        :param comparator: Function to compare elements for priority.
        :param initial_capacity: Initial capacity (not used in this implementation).
        """
        super().__init__(list_type=None)  # Default list_type is None; can be ArrayList or LinkedList
        self.comparator = comparator
        self._heap = []  # Internal heap to store elements in heap order

        # Add initial elements to the priority queue
        if isinstance(initial, Collection) or isinstance(initial, list):
            for item in initial:
                self.add(item)
        elif initial:
            raise TypeError("Initial input must be a Collection or None")

    def add(self, e):
        """
        Adds an element to the priority queue.

        :param e: The element to add.
        :return: True if the element was successfully added.
        """
        if self.comparator:
            heappush(self._heap, (self.comparator(e), e))
        else:
            heappush(self._heap, e)
        return True

    def offer(self, e):
        """
        Adds an element to the priority queue. Same as `add()`.

        :param e: The element to add.
        :return: True if the element was successfully added.
        """
        return self.add(e)

    def peek(self):
        """
        Retrieves but does not remove the highest-priority element from the queue.

        :return: The highest-priority element, or None if the queue is empty.
        """
        if self.isEmpty():
            return None
        return self._heap[0][1] if self.comparator else self._heap[0]

    def poll(self):
        """
        Removes and returns the highest-priority element from the queue.

        :return: The highest-priority element, or None if the queue is empty.
        """
        if self.isEmpty():
            return None
        return heappop(self._heap)[1] if self.comparator else heappop(self._heap)

    def remove(self, o):
        """
        Removes a specific element from the queue.

        :param o: The element to remove.
        :return: True if the element was successfully removed, False otherwise.
        """
        try:
            self._heap.remove(o)
            heapify(self._heap)  # Re-heapify the heap after removing the element
            return True
        except ValueError:
            return False

    def contains(self, o):
        """
        Checks if the queue contains a specific element.

        :param o: The element to check for.
        :return: True if the element is present, False otherwise.
        """
        return o in self._heap

    def size(self):
        """
        Returns the number of elements in the queue.

        :return: The number of elements.
        """
        return len(self._heap)

    def clear(self):
        """
        Removes all elements from the queue.
        """
        self._heap = []

    def isEmpty(self):
        """
        Checks if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return len(self._heap) == 0

    def iterator(self):
        """
        Returns an iterator over the elements in the queue.

        :return: An iterator for the queue.
        """
        return iter(self._heap)

    def toArray(self):
        """
        Converts the queue to a list.

        :return: A list of elements in the queue.
        """
        return list(self._heap)

    def toArrayWithType(self, arr):
        """
        Converts the queue to an array with the runtime type of the specified array.

        :param arr: The array type to convert to.
        :return: A list of elements in the queue.
        """
        return list(self._heap)

    def comparator(self):
        """
        Returns the comparator function used for the priority queue.

        :return: The comparator function.
        """
        return self.comparator

    def spliterator(self):
        """
        Returns a spliterator (not implemented).

        :return: None.
        """
        pass

    def addAll(self, collection):
        """
        Adds all elements from another collection to the queue.

        :param collection: The collection of elements to add.
        """
        for item in collection:
            self.add(item)

    def element(self):
        """
        Retrieves but does not remove the highest-priority element.

        :return: The highest-priority element.
        :raises IndexError: If the queue is empty.
        """
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.peek()

    def removeAll(self, collection):
        """
        Removes all elements that are also contained in the specified collection.

        :param collection: The collection of elements to remove.
        """
        for item in collection:
            self.remove(item)

    def retainAll(self, collection):
        """
        Retains only the elements contained in the specified collection.

        :param collection: The collection to retain.
        """
        self._heap = [item for item in self._heap if item in collection]
        heapify(self._heap)

    def __iter__(self):
        """
        Returns an iterator over the elements in the priority queue.

        :return: An iterator for the queue.
        """
        return iter(self._heap)

    def containsAll(self, collection):
        """
        Checks if all elements in the given collection are in the queue.

        :param collection: The collection to check.
        :return: True if all elements are present, False otherwise.
        """
        return all(item in self._heap for item in collection)

    def equals(self, other):
        """
        Compares this queue with another for equality.

        :param other: The queue to compare with.
        :return: True if the queues have the same elements, False otherwise.
        """
        if not isinstance(other, PriorityQueue):
            return False
        return self._heap == other._heap

    def hashCode(self):
        """
        Returns the hash code for this queue.

        :return: The hash code.
        """
        return hash(tuple(self._heap))

    def removeIf(self, predicate):
        """
        Removes all elements that satisfy the given predicate.

        :param predicate: The predicate to evaluate.
        """
        self._heap = [item for item in self._heap if not predicate(item)]
        heapify(self._heap)

    def stream(self):
        """
        Returns a generator for the elements in the queue.

        :return: A generator for the elements.
        """
        return iter(self._heap)

    def parallelStream(self):
        """
        Returns a parallel stream (not applicable in Python).

        :return: A normal stream (iterator).
        """
        return self.stream()
