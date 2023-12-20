#!/usr/bin/python3

class Square:
    """
    Class Square that defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
          - size: The size of the square (default is 0).
          - position: The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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
          - TypeError: If size is not an integer.
          - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
          - The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Parameters:
          - value: The value to set as the position of the square.

        Raises:
          - TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(x, int) for x in value)
            or not all(x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
          - The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        String representation of the square.

        Returns:
          - str: The square as a string.
        """
        return self.my_print()


# Example Usage:
# square = Square(4, (1, 2))
# square.my_print()

