#!/usr/bin/python3
import math

class MagicClass:
    """
    Python class MagicClass that replicates the given Python bytecode.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass class.

        Parameters:
          - radius: The radius of the circle (default is 0).
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Computes the area of the circle.

        Returns:
          - The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes the circumference of the circle.

        Returns:
          - The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

# Example Usage:
# magic_circle = MagicClass(5)
# print(magic_circle.area())  # Output: 78.53981633974483
# print(magic_circle.circumference())  # Output: 31.41592653589793


