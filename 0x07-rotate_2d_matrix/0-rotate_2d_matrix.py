#!/usr/bin/python3
'''
0-rotate_2d_matrix
'''


def rotate_2d_matrix(matrix):
    '''
    python scricpt to rotate a 2d matrix
    '''
    _mat = matrix
    mat = list(zip(*matrix[::-1]))
    for i, val in enumerate(mat):
        mat[i] = list(val)

    for i, val in enumerate(mat):
        for j, v in enumerate(val):
            _mat[i][j] = v
