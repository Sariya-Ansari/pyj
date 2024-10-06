"""
This module defines the `Vector` class, a dynamic array-like data structure similar to the Java Vector class.

Classes:
    - Vector: A resizable array that supports dynamic resizing, inserting, removing, and iterating over elements.

Attributes:
    - capacityIncrement: Defines how much to increase the vector's capacity when it exceeds the current limit.
    - elementData: Internal list to hold the elements of the vector.
    - elementCount: The number of elements currently stored in the vector.

Methods:
    - ensureCapacity: Ensures that the vector has at least a specified capacity.
    - addElement: Adds an element to the vector.
    - add: Adds an element to the vector or inserts it at a specified index.
    - addAll: Adds all elements from a collection or iterable to the vector.
    - clear: Removes all elements from the vector.
    - contains: Checks if the vector contains a specific element.
    - containsAll: Checks if the vector contains all elements of a collection.
    - clone: Creates a shallow copy of the vector.
    - copyInto: Copies the vector's elements into an array.
    - elementAt: Returns the element at a specified index.
    - elements: Returns an iterator for the vector's elements.
    - firstElement: Returns the first element of the vector.
    - lastElement: Returns the last element of the vector.
    - equals: Compares the vector for equality with another vector.
    - get: Returns the element at a specified index.
    - hashCode: Returns a hash code for the vector based on its elements.
    - indexOf: Returns the index of the first occurrence of a specific element.
    - isEmpty: Checks if the vector is empty.
    - iterator: Returns an iterator for the vector's elements.
    - lastIndexOf: Returns the index of the last occurrence of a specific element.
    - listIterator: Returns an iterator for a portion of the vector starting at a specified index.
    - removeElement: Removes a specific element from the vector.
    - remove: Removes an element from the vector by index or value.
    - removeAll: Removes all elements from the vector that are contained in a collection.
    - trimToSize: Trims the vector's capacity to match its current size.
    - setSize: Sets the size of the vector.
    - setElementAt: Sets the value of an element at a specific index.
    - removeElementAt: Removes the element at a specific index.
    - removeAllElements: Removes all elements from the vector.
    - replaceAll: Replaces each element with the result of applying a function.
    - retainAll: Retains only the elements that are in a specified collection.
    - set: Sets the element at a specific index and returns the old element.
    - size: Returns the number of elements in the vector.
    - sort: Sorts the elements of the vector.
    - spliterator: Returns an iterator for the vector's elements.
    - subList: Returns a sublist of the vector.
    - toArray: Converts the vector to an array.
    - __iter__: Implements the iterable interface for the vector.
    - parallelStream: Returns an iterator for the vector's elements (not parallel).
    - removeIf: Removes elements that satisfy a predicate.
    - stream: Returns an iterator for the vector's elements.
"""

from jcollections.collection import Collection
from jcollections.list import List


class Vector(List):
    """
    A dynamic array-like data structure similar to the Java Vector class.

    The `Vector` class supports dynamic resizing, allowing elements to be added or removed,
    with automatic resizing of the underlying storage array. It provides methods for insertion,
    deletion, and iteration over elements, similar to the behavior of Java's `Vector` class.

    Attributes:
        capacityIncrement (int): Defines how much to increase the vector's capacity when needed.
        elementData (list): Internal list holding the vector's elements.
        elementCount (int): The number of elements currently in the vector.

    Methods:
        - add: Adds an element or inserts at a specific index.
        - remove: Removes an element by index or value.
        - ensureCapacity: Ensures the vector has a specified minimum capacity.
        - and many more...
    """

    def __init__(self, *args):
        """
        Initializes a new instance of the Vector class.
        Handles multiple cases based on the number and type of arguments passed:
        - No arguments: Initializes an empty vector with a default capacity of 10.
        - Single integer argument: Initializes the vector with the specified initial capacity.
        - Single Collection argument: Initializes the vector with elements from the provided collection.
        - Two integer arguments: Initializes the vector with a specified initial capacity and capacity increment.
        """
        if len(args) == 0:
            self.capacityIncrement = 0
            self.elementData = [None] * 10
            self.elementCount = 0

        elif len(args) == 1 and isinstance(args[0], int):
            self.capacityIncrement = 0
            self.elementData = [None] * args[0]
            self.elementCount = 0

        elif len(args) == 1 and isinstance(args[0], Collection):
            self.capacityIncrement = 0
            self.elementData = list(args[0])
            self.elementCount = len(self.elementData)

        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            initialCapacity, self.capacityIncrement = args
            self.elementData = [None] * initialCapacity
            self.elementCount = 0

    def ensureCapacity(self, min_capacity):
        """
        Ensures that the vector's capacity is at least min_capacity.
        Expands the capacity if necessary, based on the capacity increment or doubling the current size.
        """
        if min_capacity > len(self.elementData):
            new_capacity = len(self.elementData) + self.capacityIncrement if self.capacityIncrement > 0 else len(self.elementData) * 2
            if new_capacity < min_capacity:
                new_capacity = min_capacity
            new_data = [None] * new_capacity
            for i in range(self.elementCount):
                new_data[i] = self.elementData[i]
            self.elementData = new_data

    def addElement(self, obj):
        """
        Adds the specified element to the end of this vector, increasing its size by one.
        """
        if self.elementCount == len(self.elementData):
            self.ensureCapacity(len(self.elementData) + (self.capacityIncrement if self.capacityIncrement > 0 else len(self.elementData)))
        self.elementData[self.elementCount] = obj
        self.elementCount += 1

    def add(self, *args):
        """
        Adds an element to the vector.
        Handles two cases:
        - Single argument: Adds the element to the end of the vector.
        - Two arguments: Inserts the element at the specified index, shifting existing elements as needed.
        """
        if len(args) == 1:
            element = args[0]
            self.ensureCapacity(self.elementCount + 1)
            self.elementData[self.elementCount] = element
            self.elementCount += 1
            return True
        elif len(args) == 2:
            index, element = args
            if index > self.elementCount or index < 0:
                raise IndexError("Index out of bounds")
            self.ensureCapacity(self.elementCount + 1)
            for i in range(self.elementCount, index, -1):
                self.elementData[i] = self.elementData[i - 1]
            self.elementData[index] = element
            self.elementCount += 1

    def addAll(self, *args):
        """
        Appends or inserts all elements from the specified collection or iterable into this vector.
        - Single argument: Appends elements from the provided collection.
        - Two arguments: Inserts elements from the provided collection at the specified index.
        """
        if len(args) == 1:
            collection = args[0]
            if not isinstance(collection, Collection):
                if hasattr(collection, '__iter__'):
                    collection = list(collection)
                else:
                    raise TypeError("Argument must be an iterable or of type Collection")
            newElementCount = len(collection)
            if newElementCount == 0:
                return False
            self.ensureCapacity(self.elementCount + newElementCount)
            for element in collection:
                self.elementData[self.elementCount] = element
                self.elementCount += 1
            return True

        elif len(args) == 2:
            index, collection = args
            if not isinstance(collection, Collection):
                if hasattr(collection, '__iter__'):
                    collection = list(collection)
                else:
                    raise TypeError("Argument must be an iterable or of type Collection")
            if index < 0 or index > self.elementCount:
                raise IndexError("Index out of bounds")
            newElementCount = len(collection)
            if newElementCount == 0:
                return False
            self.ensureCapacity(self.elementCount + newElementCount)
            for i in range(self.elementCount - 1, index - 1, -1):
                self.elementData[i + newElementCount] = self.elementData[i]
            for element in collection:
                self.elementData[index] = element
                index += 1
            self.elementCount += newElementCount
            return True

    def clear(self):
        """
        Clears the vector by resetting all elements to None and setting the element count to 0.
        """
        self.elementData = [None] * len(self.elementData)
        self.elementCount = 0

    def contains(self, o):
        """
        Checks if the vector contains the specified element.

        :param o: The element to check for.
        :return: True if the element is present, False otherwise.
        """
        return o in self.elementData[:self.elementCount]

    def containsAll(self, c):
        """
        Checks if the vector contains all elements of the specified collection.

        :param c: The collection to check for containment.
        :return: True if all elements are present, False otherwise.
        """
        return all(elem in self.elementData[:self.elementCount] for elem in c)

    def clone(self):
        """
        Returns a new Vector instance that is a clone of the current vector, including a copy of its elements.

        :return: A new Vector object that is a shallow copy of this vector.
        """
        cloned_vector = Vector(len(self.elementData), self.capacityIncrement)
        cloned_vector.elementData = self.elementData[:self.elementCount] + [None] * (len(self.elementData) - self.elementCount)
        cloned_vector.elementCount = self.elementCount
        return cloned_vector

    def copyInto(self, anArray):
        """
        Copies the elements of the vector into the specified array.
        Raises a ValueError if the destination array is not large enough.

        :param anArray: The array to copy elements into.
        """
        if len(anArray) < self.elementCount:
            raise ValueError("Destination array is not large enough.")
        for i in range(self.elementCount):
            anArray[i] = self.elementData[i]

    def elementAt(self, index):
        """
        Returns the element at the specified index.
        Raises an IndexError if the index is out of bounds.

        :param index: The index of the element to retrieve.
        :return: The element at the specified index.
        """
        if index < 0 or index >= self.elementCount:
            raise IndexError("Index out of bounds.")
        return self.elementData[index]

    def elements(self):
        """
        Returns an iterator over the elements of the vector.

        :return: An iterator for the elements in the vector.
        """
        return iter(self.elementData[:self.elementCount])

    def firstElement(self):
        """
        Returns the first element of the vector.
        Raises an IndexError if the vector is empty.

        :return: The first element in the vector.
        """
        if self.elementCount == 0:
            raise IndexError("Vector is empty.")
        return self.elementData[0]

    def lastElement(self):
        """
        Returns the last element of the vector.
        Raises an IndexError if the vector is empty.

        :return: The last element in the vector.
        """
        if self.elementCount == 0:
            raise IndexError("Vector is empty.")
        return self.elementData[self.elementCount - 1]

    @property
    def __class__(self):
        """
        Returns the class of the current instance.
        """
        return super().__class__

    def equals(self, o):
        """
        Compares the current vector to another vector for equality.
        Returns True if they are equal, False otherwise.

        :param o: The object to compare with.
        :return: True if the objects are equal, False otherwise.
        """
        if not isinstance(o, Vector):
            return False
        if self.size() != o.size():
            return False
        for i in range(self.size()):
            if self.elementData[i] != o.elementData[i]:
                return False
        return True

    def get(self, index):
        """
        Returns the element at the specified index.
        Raises an IndexError if the index is out of bounds.

        :param index: The index of the element to retrieve.
        :return: The element at the specified index.
        """
        if index < 0 or index >= self.elementCount:
            raise IndexError("Index out of bounds.")
        return self.elementData[index]

    def hashCode(self):
        """
        Returns a hash code for the vector based on its elements.

        :return: The hash code of the vector.
        """
        result = 1
        for element in self.elementData[:self.elementCount]:
            result = 31 * result + (element if element is not None else 0)
        return result

    def indexOf(self, o):
        """
        Returns the index of the first occurrence of the specified element.
        Returns -1 if the element is not found.

        :param o: The element to search for.
        :return: The index of the element, or -1 if not found.
        """
        for i in range(self.elementCount):
            if self.elementData[i] == o:
                return i
        return -1

    def isEmpty(self):
        """
        Checks if the vector is empty.

        :return: True if the vector is empty, False otherwise.
        """
        return self.elementCount == 0

    def iterator(self):
        """
        Returns an iterator over the elements of the vector.

        :return: An iterator for the vector.
        """
        return iter(self.elementData[:self.elementCount])

    def lastIndexOf(self, o):
        """
        Returns the index of the last occurrence of the specified element.
        Returns -1 if the element is not found.

        :param o: The element to search for.
        :return: The index of the element, or -1 if not found.
        """
        for i in range(self.elementCount - 1, -1, -1):
            if self.elementData[i] == o:
                return i
        return -1

    def listIterator(self, *args):
        """
        Returns a list iterator over the vector:
        - No arguments: Returns an iterator over all elements.
        - Single argument: Returns an iterator starting from the specified index.

        :param args: The starting index for the iterator (optional).
        :return: An iterator for the elements in the vector.
        """
        if len(args) == 0:
            return iter(self.elementData[:self.elementCount])
        elif len(args) == 1:
            index = args[0]
            if index < 0 or index > self.elementCount:
                raise IndexError("Index out of bounds.")
            return iter(self.elementData[index:self.elementCount])
        else:
            raise TypeError("Invalid number of arguments.")

    def removeElement(self, *args):
        """
        Removes the specified element from the vector.
        Returns True if the element was removed, False otherwise.

        :param args: The element to remove.
        :return: True if the element was removed, False otherwise.
        """
        if len(args) == 1:
            element = args[0]
            try:
                index = self.indexOf(element)
                if index != -1:
                    self.__removeAt__(index)
                    return True
                return False
            except IndexError:
                return False

    def remove(self, *args):
        """
        Removes an element from the vector:
        - Single integer argument: Removes the element at the specified index.
        - Single non-integer argument: Removes the first occurrence of the specified value.

        :param args: The index or value to remove.
        :return: The removed element, or True/False for value removal.
        """
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, int):
                return self.__removeAt__(arg)
            else:
                return self.removeElement(arg)
        else:
            raise TypeError("Invalid number of arguments.")

    def __removeAt__(self, index):
        """
        Removes the element at the specified index and returns it.
        Shifts remaining elements to fill the gap.
        Raises an IndexError if the index is out of bounds.

        :param index: The index of the element to remove.
        :return: The removed element.
        """
        if index < 0 or index >= self.elementCount:
            raise IndexError("Index out of bounds.")

        removed_element = self.elementData[index]
        for i in range(index, self.elementCount - 1):
            self.elementData[i] = self.elementData[i + 1]
        self.elementData[self.elementCount - 1] = None
        self.elementCount -= 1

        return removed_element

    def removeAll(self, c):
        """
        Removes all elements contained in the specified collection.
        Returns True if any elements were removed.

        :param c: The collection of elements to remove.
        :return: True if any elements were removed, False otherwise.
        """
        removed = False
        for elem in c:
            while self.removeElement(elem):
                removed = True
        return removed

    def trimToSize(self):
        """
        Trims the capacity of the vector to its current size.
        """
        if len(self.elementData) > self.elementCount:
            self.elementData = self.elementData[:self.elementCount]

    def setSize(self, newSize):
        """
        Sets the size of the vector.
        Expands or shrinks the vector as necessary.

        :param newSize: The new size of the vector.
        """
        if newSize < 0:
            raise ValueError("New size must be non-negative.")
        if newSize > len(self.elementData):
            self.ensureCapacity(newSize)
        elif newSize < self.elementCount:
            for i in range(newSize, self.elementCount):
                self.elementData[i] = None
        self.elementCount = newSize

    def setElementAt(self, value, index):
        """
        Sets the element at the specified index to the provided value.
        Expands the vector if the index is beyond the current element count.

        :param value: The new value to set.
        :param index: The index to set the value at.
        """
        if index < 0:
            raise IndexError("Index out of bounds.")
        if index >= len(self.elementData):
            self.ensureCapacity(index + 1)
        if index >= self.elementCount:
            self.elementCount = index + 1
        self.elementData[index] = value

    def removeElementAt(self, index):
        """
        Removes the element at the specified index using the private __removeAt__ method.

        :param index: The index of the element to remove.
        """
        return self.__removeAt__(index)

    def removeAllElements(self):
        """
        Removes all elements from the vector and resets the element count to 0.
        """
        self.clear()

    def replaceAll(self, operator):
        """
        Replaces each element of the vector with the result of applying the specified operator function.

        :param operator: A function to apply to each element.
        """
        for i in range(self.elementCount):
            self.elementData[i] = operator(self.elementData[i])

    def retainAll(self, c):
        """
        Retains only the elements that are contained in the specified collection.
        Returns True if any elements were removed.

        :param c: The collection to retain elements from.
        :return: True if any elements were removed, False otherwise.
        """
        removed = False
        for i in range(self.elementCount):
            if self.elementData[i] not in c:
                self.__removeAt__(i)
                removed = True
        return removed

    def set(self, index, element):
        """
        Sets the element at the specified index to the provided value.
        Returns the old element at that index.

        :param index: The index of the element to set.
        :param element: The new value to set.
        :return: The old value at the specified index.
        """
        if index < 0 or index >= self.elementCount:
            raise IndexError("Index out of bounds.")
        old_value = self.elementData[index]
        self.elementData[index] = element
        return old_value

    def size(self):
        """
        Returns the number of elements in the vector.

        :return: The number of elements in the vector.
        """
        return self.elementCount

    def sort(self, c):
        """
        Sorts the elements of the vector using the provided comparator function.

        :param c: The comparator function to use for sorting.
        """
        self.elementData[:self.elementCount] = sorted(self.elementData[:self.elementCount], key=c)

    def spliterator(self):
        """
        Returns an iterator (simplified version) for the vector's elements.

        :return: An iterator for the elements.
        """
        return iter(self.elementData[:self.elementCount])

    def subList(self, fromIndex, toIndex):
        """
        Returns a sublist of the vector from fromIndex (inclusive) to toIndex (exclusive).
        Raises an IndexError if indices are out of bounds.

        :param fromIndex: The starting index of the sublist (inclusive).
        :param toIndex: The ending index of the sublist (exclusive).
        :return: A sublist of the vector.
        """
        if fromIndex < 0 or toIndex > self.elementCount or fromIndex > toIndex:
            raise IndexError("Index out of bounds.")
        return self.elementData[fromIndex:toIndex]

    def toArray(self, *args):
        """
        Converts the vector to an array:
        - No arguments: Returns a new array containing the vector's elements.
        - Single argument: Fills the provided array with the vector's elements. Returns the array.

        :param args: Optional array to fill with the vector's elements.
        :return: An array of the vector's elements.
        """
        if len(args) == 0:
            return self.elementData[:self.elementCount]
        elif len(args) == 1:
            anArray = args[0]
            if len(anArray) < self.elementCount:
                raise ValueError("Destination array is not large enough.")
            for i in range(self.elementCount):
                anArray[i] = self.elementData[i]
            return anArray
        else:
            raise TypeError("Invalid number of arguments.")

    def __iter__(self):
        """
        Implements the iterable interface.
        Yields elements of the vector one by one.

        :return: An iterator for the vector.
        """
        for i in range(self.elementCount):
            yield self.elementData[i]

    def parallelStream(self):
        """
        Returns an iterator (not truly parallel) for the vector's elements.

        :return: An iterator for the vector.
        """
        return iter(self.elementData[:self.elementCount])

    def removeIf(self, predicate):
        """
        Removes all elements that satisfy the given predicate.
        Returns True if any elements were removed.

        :param predicate: A function that returns True for elements to remove.
        :return: True if any elements were removed, False otherwise.
        """
        removed = False
        for i in range(self.elementCount - 1, -1, -1):
            if predicate(self.elementData[i]):
                self.__removeAt__(i)
                removed = True
        return removed

    def stream(self):
        """
        Returns a sequential iterator for the vector's elements.

        :return: An iterator for the vector's elements.
        """
        return iter(self.elementData[:self.elementCount])
