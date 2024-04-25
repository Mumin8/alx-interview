#!/usr/bin/python3
'''
0-rotate_2d_matrix
'''


def rotate_2d_matrix(matrix):
    '''
    python scricpt to rotate a 2d matrix
    '''
    return list(zip(*matrix[::-1]))
