#!/usr/bin/python3
"""
This module contains a function that divides all
The matrix is a list of lists of integers or floats.
The function raises errors if the input is invalid.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number, rounding.

    Parameters:
    matrix (list of lists): The matrix (list of lists).
    div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with each element divided.

    Raises:
    TypeError: If matrix is not a list of lists of integers.
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
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1, 2], [3]], 2)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size
    """

    error = "matrix must be a matrix (list of lists) of integers/floats"
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(error)

    # Check if all rows of the matrix have the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError(error)

    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Handle the case when div is infinity or NaN
    if div == float('inf') or div == float('-inf') or div != div:  # NaN check
        raise TypeError("div must be a number")

    # Handle the case when matrix contains inf or nan values
    result_matrix = []
    for row in matrix:
        result_row = []
        for elem in row:
            if elem == float('inf') or elem == float('-inf'):
                result_row.append(0.0)
            elif elem != elem:  # Check for NaN
                result_row.append(0.0)
            else:
                result_row.append(round(elem / div, 2))
        result_matrix.append(result_row)

    return result_matrix
