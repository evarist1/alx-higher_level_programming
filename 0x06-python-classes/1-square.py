#!/usr/bin/python3
class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Size must be a positive integer")
        self.__size = size
