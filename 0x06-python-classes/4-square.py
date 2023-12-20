#!/usr/bin/python3

class Square:
    """
    Class Square that defines a square with a private instance attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
          - size (int): The size of the square (default is 0).
        """
        self.__size = size

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

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
          - int: The area of the square.
        """
        return self.__size ** 2

