from typing import Callable

def rotateMatrix(M : list[int]) -> list[int]:
    temp = 0
    dim = len(M)
    result = [[0 for i in range(dim)] for j in range(dim)]
    for row_num, row in enumerate(M):
        for col_num, element in enumerate(row):
            result[col_num][(dim - 1) - row_num] = element

    return result


# Going to acheive this by exploiting the fact that for any given location being written into
#  we could process that location to save the info and this leads to loops of length 4
#  for example the top left corner gets placed into the top right, top right into bottom right, 
#  bottom right into bottom left, bottom left into top right (loop complete)
#  So we can swap these 4 around all at once and lose no information
#
# Technically since this is done in place and arrays are pass by reference we don't need to return
#  but for ease of testing I have left the return in
#
# O(n^2)
def rotate_matrix_in_place(M : list[int]) -> list[int]:
    dim = len(M)
    for row_num in range(dim // 2):                         # O(n) <- O(n-1)
        for col_num in range(row_num, (dim - 1) - row_num): # O(n) <- O(fraction of n but the fraction scales linearly)
            current = (row_num, col_num)
            next = (col_num, (dim - 1) - row_num)
            to_write = M[current[0]][current[1]]
            temp = 0
            for i in range(4):                              # O(1) <- O(4)
                temp = M[next[0]][next[1]]
                M[next[0]][next[1]] = to_write
                current = next
                next = (current[1], (dim - 1) - current[0])
                to_write = temp
                
    return M


def print_matrix(M : list[int]):
    for row in M:
        print(row)


def test(func_version : Callable = rotateMatrix ):
    cases = [
        [
        [1,2],
        [3,4]
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
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
        ]
    ]
    
    for case in cases:
        print_matrix(case)
        print("Rotated below")
        print_matrix(func_version(case))
        print()

test(rotate_matrix_in_place)