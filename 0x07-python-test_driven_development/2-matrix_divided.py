
dule for matrix_divided method."""


def matrix_divided(matrix, div):
        """Divides all elements of the matrix by div.

            Args:
                        matrix: List of lists containing integers or floats.
                                div: Number to divide the matrix by.

                                    Returns:
                                                list: List of lists representing the divided matrix.

                                                    Raises:
                                                                TypeError: If matrix is not a list of lists containing integers or floats.
                                                                        TypeError: If sublists are not all of the same size.
                                                                                TypeError: If div is not an integer or float.
                                                                                        ZeroDivisionError: If div is zero.
                                                                                            """
                                                                                                if not isinstance(div, (int, float)):
                                                                                                        raise TypeError("div must be a number")
                                                                                                            if not isinstance(matrix, list) or len(matrix) == 0:
                                                                                                                    raise TypeError("matrix must be a matrix (list of lists) " +
                                                                                                                                            "of integers/floats")
                                                                                                                                                for row in matrix:
                                                                                                                                                        if not isinstance(row, list) or len(row) == 0:
                                                                                                                                                                    raise TypeError("matrix must be a matrix (list of lists) " +
                                                                                                                                                                                                "of integers/floats")
                                                                                                                                                                                                        if len(row) != len(matrix[0]):
                                                                                                                                                                                                                    raise TypeError("Each row of the matrix must have the same size")
                                                                                                                                                                                                                            for x in row:
                                                                                                                                                                                                                                        if not isinstance(x, (int, float)):
                                                                                                                                                                                                                                                        raise TypeError("matrix must be a matrix (list of lists) " +
                                                                                                                                                                                                                                                                                        "of integers/floats")
                                                                                                                                                                                                                                                                                            return [[round(x / div, 2) for x in row] for row in matrix]

                                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                import doctest
                                                                                                                                                                                                                                                                                                    doctest.testfile("tests/2-matrix_divided.txt")
