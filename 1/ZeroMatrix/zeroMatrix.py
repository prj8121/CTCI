from typing import Callable
import numpy as np

# Wrote this before importing numpy for the matrix multiplication version,
#   so this function still has a lot of code that could be made shorter using numpy 
def zeroMatrix(matrix : list) -> list:
    M = len(matrix)
    N = len(matrix[0])
    rows_to_zero = set()
    cols_to_zero = set()
    for row_num in range(M):
        for col_num in range(N):
            if matrix[row_num][col_num] == 0:
                rows_to_zero.add(row_num)
                cols_to_zero.add(col_num)

    result = matrix.copy()
    for row_num in rows_to_zero:
        result[row_num] = [0 for x in matrix[row_num]]
    
    for col_num in cols_to_zero:
        for row_num in range(M):
            result[row_num][col_num] = 0

    return result


def zeroMatrixByMultiplying(matrix : list) -> list:
    row_products = np.array(np.prod(matrix, axis=1))
    col_products = np.array(np.prod(matrix, axis=0))
    row_products[row_products != 0] = 1
    col_products[col_products != 0] = 1

    matrix = matrix * row_products[:, np.newaxis]
    matrix = matrix * col_products
    return matrix


def print_matrix(M : list[int]):
    for row in M:
        print(row)


def test(func_version : Callable = zeroMatrix ):
    cases = [
        [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,0]
        ],
        [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [0,9]
        ],
        [
        [1,2],
        [3,4],
        [5,6],
        [0,8],
        [9,0]
        ],
        [
        [1,2],
        [3,4],
        [5,0],
        [7,8],
        [9,0]
        ],
        [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ],
        [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ],
        [
        [1,2,0,4,5],
        [6,0,8,9,10],
        [11,12,13,14,15],
        [16,0,18,19,20],
        [21,22,23,24,25]
        ]
    ]
    
    for case in cases:
        print_matrix(case)
        print("Zeroed below")
        print_matrix(func_version(case))
        print()

test(zeroMatrixByMultiplying)
