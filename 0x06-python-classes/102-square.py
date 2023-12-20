#!/usr/bin/python3
"""
Module for Square class.
"""

class Square:
    """
    Class Square that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
          - size: The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
          - The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
          - value: The value to set as the size of the square.

        Raises:
          - TypeError: If size is not a number (float or integer).
          - ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
          - The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparator.

        Parameters:
          - other: The other Square object to compare.

        Returns:
          - bool: True if areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Inequality comparator.

        Parameters:
          - other: The other Square object to compare.

        Returns:
          - bool: True if areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Greater than comparator.

        Parameters:
          - other: The other Square object to compare.

        Returns:
          - bool: True if area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Greater than or equal to comparator.

        Parameters:
          - other: The other Square object to compare.

        Returns:
          - bool: True if area is greater or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Less than comparator.

        Parameters:
          - other: The other Square object to compare.

        Returns:
          - bool: True if area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal to comparator.

        Parameters:
          - other: The other Square object to compare.

        Returns:
          - bool: True if area is less or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

# Example Usage:
# square1 = Square(4)
# square2 = Square(5)
# print(square1 == square2)  # False
# print(square1 != square2)  # True
# print(square1 > square2)   # False
# print(square1 >= square2)  # False
# print(square1 < square2)   # True
# print(square1 <= square2)  # True

