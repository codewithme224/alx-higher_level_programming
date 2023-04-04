#!/usr/bin/python3
"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
     Args:
        matrix: a 2d array, each row should be the same size or else: error
        div: a number that is not 0 or else error
    Returns: a new matrix with each element adjusted to the div amount
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    # Check if matrix is valid
    if not all(
        isinstance(row, list)
        and all(
            isinstance(x, (int, float))
            for x in row
        )
        for row in matrix
    ):
        raise TypeError(msg)

    # Check if div is valid
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if each row of matrix has the same length
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
