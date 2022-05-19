"""SEARCH IN MATRIX
--------

You are given a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT """
import numpy as np

matrix = np.array([
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
])

# this prints the row and column with number 44 in it
# print(column_containing_target = (matrix[3, :]))
# print(row_containing_target = (matrix[:, 3]))


# EXAMPLE OUTPUT

def search_in_matrix(matrix, target):
    ans = []
    target = np.where(matrix == target)
    column_and_row = list(zip(target[0], target[1]))
    for indices in column_and_row:
        ans.append(indices[0])
        ans.append(indices[1])
        return ans
    if target not in matrix:
        return[-1, -1]


print(search_in_matrix(matrix, 44))
# this way^ comes up with a warning- no errors however

# alternative way of doing it below- works just fine


def search_in_matrix2(matrix, target):
    if not matrix or not matrix[0]:
        return[1, -1]
    for x, y in enumerate(matrix):
        for z, index in enumerate(y):
            if index == target:
                return [x, z]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

print(search_in_matrix2(matrix, 44))
