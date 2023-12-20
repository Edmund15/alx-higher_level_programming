#!/usr/bin/python3
"""
Module: 8-square
Defines a Square class with size and position attributes and methods
to calculate area and print the square
"""


class Square:
    """
    Square class that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (must be an integer >= 0).
            position (tuple): The position of the square (must be a tuple of 2 positive integers).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value: The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square.

        Args:
            value: The position to set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # to stdout.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __lt__(self, other):
        """
        Less than comparison method for comparing two Square instances.

        Args:
            other: The other Square instance to compare.

        Returns:
            bool: True if self is less than other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison method for comparing two Square instances.

        Args:
            other: The other Square instance to compare.

        Returns:
            bool: True if self is less than or equal to other, False otherwise.
        """
        return self.area() <= other.area()


if __name__ == "__main__":
    # Example usage:
    s_5 = Square(5)
    s_6 = Square(6)
    if s_5 <= s_6:
        print("s_5 is smaller than or equal to s_6")
    else:
        print("s_5 is not smaller than or equal to s_6")

