#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Raj Mahal"

import math 

def add(x, y):
    """Add two integers. Handles negative values."""
    
    return x + y


def multiply(x, y):
    if y < 0:
        return -multiply(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply(x, y - 1)


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
