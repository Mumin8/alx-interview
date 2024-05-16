#!/usr/bin/python3
import copy

'''0-prime_game'''


def isWinner(x, nums):
    '''isWinner function'''
    print(nums)
    _nums = copy.deepcopy(nums)
    prime = [True for i in range(x + 1)]
    p = 2
    while (p * p <= x):
        if (prime[p]):

            for i in range(p * p, x + 1, p):
                prime[i] = False
        p += 1
    prime_ = []
    for p in range(2, x + 1):
        if prime[p]:
            prime_.append(p)

    count = 1
    for pn in prime_:

        l = len(_nums)
        _nums = list(filter(lambda x: x % pn, _nums))
        _nums = _nums
        if l > len(_nums):
            count += 1
            prime_.pop(0)
        else:
            break

    if count % 2 == 0:
        return "Maria"
    else:
        return "Ben"
