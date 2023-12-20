#!/user/bin/python3

"""
Module: 1-square
Defines a square with private attribute size
"""

class Square:
    """
    Represents a square
    """

    def __init__(self,size):
       
        """
        Initializes a new Square instance

        Parameters:
        - size (int): The size of the square.

        Note:
	The size attribute is a private instance attribute.
        """        
        self.__size = size
