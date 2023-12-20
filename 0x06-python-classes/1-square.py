#!/usr/bin/python3
"""
Module: 1-square
Defines a Square class with a private instance attribute size
"""


class Square:
    """
    Square class with a private instance attribute size
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private.
        """
        self.__size = size

