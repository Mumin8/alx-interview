#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    return list(zip(*matrix[::-1]))
    