#!/usr/bin/python3
"""
This module contains a function that divides all elements
The matrix is a list of lists of integers or floats,
The function raises errors if the input is invalid,
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number,

    Parameters:
    matrix (list of lists): The matrix (list of list
    div (int or float): The divisor (must be a number and

    Returns:
    list of lists: A new matrix with each element divided by

    Raises:
    TypeError: If matrix is not a list of lists of integers or
    TypeError: If div is not a number.
    ZeroDivisionError: If div is zero.

    Example:
    >>> matrix_divided([[1, 2], [3, 4]], 2)
    [[0.5, 1.0], [1.5, 2.0]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    >>> matrix_divided([[1, "2"], [3, 4]], 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists)
    >>> matrix_divided([[1, 2], [3]], 2)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows of the matrix have the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]
