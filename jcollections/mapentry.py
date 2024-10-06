"""
This module defines the `MapEntry` class, which represents a key-value pair in a map-like data structure.
It allows for the retrieval, modification, and comparison of key-value pairs.

Classes:
    - MapEntry: A generic class that stores a key-value pair.
"""

from typing import TypeVar, Generic

# Define type variables K and V
K = TypeVar('K')
V = TypeVar('V')


class MapEntry(Generic[K, V]):
    """
    Represents a key-value pair (entry) in a map. Provides methods for retrieving the key and value,
    setting a new value, and comparing two entries.

    Type Parameters:
        K: The type of keys maintained by this entry.
        V: The type of mapped values.
    """

    def __init__(self, key: K, value: V):
        """
        Initializes a new MapEntry with the given key and value.

        :param key: The key for the entry.
        :param value: The value associated with the key.
        """
        self._key = key
        self._value = value

    def getKey(self) -> K:
        """
        Returns the key of the entry.

        :return: The key of the entry.
        """
        return self._key

    def getValue(self) -> V:
        """
        Returns the value of the entry.

        :return: The value associated with the key.
        """
        return self._value

    def setValue(self, value: V) -> V:
        """
        Sets a new value for the entry and returns the old value.

        :param value: The new value to set.
        :return: The old value before the update.
        """
        old_value = self._value
        self._value = value
        return old_value

    def equals(self, o) -> bool:
        """
        Compares this entry with another for equality.

        :param o: The object to compare with.
        :return: True if the keys and values of both entries are equal, False otherwise.
        """
        if isinstance(o, MapEntry):
            return self._key == o.getKey() and self._value == o.getValue()
        return False

    def hashCode(self) -> int:
        """
        Returns the hash code for the entry, based on the key and value.

        :return: The hash code of the entry.
        """
        return hash((self._key, self._value))

    def __repr__(self):
        """
        Returns a string representation of the entry in the form of (key, value).

        :return: A string representation of the key-value pair.
        """
        return f"({self._key}, {self._value})"
