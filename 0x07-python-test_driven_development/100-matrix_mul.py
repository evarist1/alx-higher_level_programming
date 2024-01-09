#!/usr/bin/python3
"""Module for matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Multiplies one matrix by another.
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the product
    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both matrices must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Both matrices must be lists of lists")

    if any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("Matrices can't be empty")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a) or \
       any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("Matrices should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("Each row must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrices can't be multiplied")

    res = [[] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            res[i].append(c)

    return res



if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
