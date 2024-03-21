#!/usr/bin/python3

'''this will perform a minimum operation'''


def minOperations(n):
    '''
    this will find the minimum operation
    '''

    if n < 2:
        return 0

    result = 0
    for i in range(2, n + 1):
        while n % i == 0:
            result += i
            n //= i
    return result
