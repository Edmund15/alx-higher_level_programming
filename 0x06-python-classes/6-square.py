#!/usr/bin/python3
"""
Module for Square class.
"""


class Square:
    """
    Class Square that defines a square with private instance attributes size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
          - size (int): The size of the square (default is 0).
          - position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
          - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
          - value (int): The value to set as the size of the square.

        Raises:
          - TypeError: If size is not an integer.
          - ValueError: If size is less than 0.
        """
        self.__size = value
        self.__validate_size()

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
          - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Parameters:
          - value (tuple): The value to set as the position of the square.

        Raises:
          - TypeError: If position is not a tuple of 2 positive integers.
        """
        self.__position = value
        self.__validate_position()

    def __validate_size(self):
        """
        Validates the size attribute.

        Raises:
          - TypeError: If size is not an integer.
          - ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def __validate_position(self):
        """
        Validates the position attribute.

        Raises:
          - TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(self.__position, tuple) or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(val, int) and val >= 0 for val in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
          - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#' to stdout.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

