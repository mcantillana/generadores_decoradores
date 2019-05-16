#!/usr/bin/env python
# -*- coding: utf-8 -*-


def memoize(f):
    memory = {}

    def wrapper(n):
        if n not in memory:
            memory[n] = f(n)
        return memory[n]
    return wrapper


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Utilizando Memoize
@memoize
def fib_memoize(n):
    if n < 2:
        return n
    return fib_memoize(n - 1) + fib_memoize(n - 2)


# Decorador mejorado, para visualización
def memoize_debug(f):
    memory = {}

    def wrapper(n):
        if n not in memory:
            memory[n] = f(n)
        else:
            print("Result was previously calculated: {0}".format(n))
        return memory[n]
    return wrapper


@memoize_debug
def fib_memoize(n):
    if n < 2:
        return n
    return fib_memoize(n - 1) + fib_memoize(n - 2)



if __name__ == '__main__':

    print(fibonacci(6))
    print(fib_memoize(6))