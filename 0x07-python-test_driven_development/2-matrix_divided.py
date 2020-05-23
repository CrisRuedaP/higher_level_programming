#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides elements of a matrix

    Args:
       matrix(list): a list of lists of integers or floats
       div:  number (integer or float)

    Returns:
       A new matrix

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        round_up = []
        for elements in row:
            if not isinstance(elements, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            round_up.append(round((elements/div), 2))
        new_matrix.append(round_up)
    return new_matrix
