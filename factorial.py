#!/usr/bin/env python
# -*- coding: utf-8 -*-


def memoize(f):
    memory = {}

    def wrapper(n):
        if n not in memory:
            memory[n] = f(n)
        return memory[n]
    return wrapper

@memoize
def factorial(k):
    if k < 2: return 1
    return k * factorial(k - 1)


if __name__ == '__main__':
    fact = factorial(5)
    print(fact)
