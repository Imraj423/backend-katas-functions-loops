#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Raj Mahal"


def add(x, y):
    """Add two integers. Handles negative values."""
    
    return x + y


def multiply(x, y):
    for i in x:
        return i + y


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if(n>=0):
        return multiply(x, pow(x, n-1))
    else:
        return 1
        
def factorial(x):
    return math.factorial(x)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))


if __name__ == '__main__':
   
    pass
