#!/usr/bin/python3

'''0-making_change.py'''


def makeChange(coins, total):
    if total <= 0:
        return 0

    c = sorted(coins)
    t = total
    
    count = 0
    while t > 0:
        if t - c[-1] >= 0:
            t -= c[-1]
            count += 1
        else:
            c.pop(-1)
        if t == 0:
            return count
        if len(c) == 0 or t < 0:
            break
    return -1
