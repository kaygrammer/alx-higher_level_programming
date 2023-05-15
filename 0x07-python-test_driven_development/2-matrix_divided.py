#!/usr//bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """

    # Check if matrix is a list of lists of integers or floats.
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) /of integers/floats")

    # Check if each row of the matrix is of the same size.
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number.
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is equal to 0.
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with all elements divided by div.
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
