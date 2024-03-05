#!/usr/bin/python3
"""
Defines a function to generate Pascal's Triangle up to a certain number of rows.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Parameters:
    n (int): The number of rows of Pascal's triangle to generate.

    Returns:
    List[List[int]]: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
