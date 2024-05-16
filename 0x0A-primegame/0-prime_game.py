#!/usr/bin/python3


def isWinner(x, nums):
    '''isWinner function'''

    prime = [True for i in range(x + 1)]
    p = 2
    while (p * p <= x):
        if (prime[p]):

            for i in range(p * p, x + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, x + 1):
        if prime[p]:
            print(p)

    count = 1
    for v in nums:
        temp = count
        idx = nums.index(v)
        for val in prime:
            if val == v:
                count += 1
                idx_ = prime.index(val)
                prime.pop(idx_)
                break
        if temp != count:
            nums.pop(idx)

    print(f'count {count}')
    if count % 2 == 1:
        return "Maria"
    else:
        return "Ben"
