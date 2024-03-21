def minOperations(n):
    if n == 1:
        return 0

    result = 0
    for i in range(2, n + 1):
        while n % i == 0:
            result += i
            n //= i
    return result
