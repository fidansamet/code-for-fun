"""Calculates the fibonacci number in given index."""


fib_dict = {0: 0, 1: 1}


def fibonacci(n):
    if n in fib_dict:
        return fib_dict[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    fib_dict[n] = res
    return res


print(fibonacci(5))
