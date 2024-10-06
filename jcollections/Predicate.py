"""
This module defines the `Predicate` class, which is used to encapsulate a function that evaluates a condition
and can be applied to various elements. It allows for the creation of predicates that can be reused and
applied to any item.

Classes:
    - Predicate: Encapsulates a function that returns a boolean value when called on an item.
"""

class Predicate:
    """
    Represents a functional predicate, which is a function that returns a boolean value when applied to an item.

    The `Predicate` class allows you to wrap a function and use it to evaluate a condition on any given item.
    """

    def __init__(self, func):
        """
        Initializes a new Predicate with the given function.

        :param func: A function that takes an item as input and returns a boolean value.
        """
        self.func = func

    def __call__(self, item):
        """
        Evaluates the predicate on the given item by calling the stored function.

        :param item: The item to evaluate the predicate on.
        :return: True if the condition is met, False otherwise.
        """
        return self.func(item)
