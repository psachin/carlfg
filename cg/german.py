#!/usr/bin/env python

def sum(n):
    "find the sum from 1 to n by Carl Friedrich Guass method"
    try:
        n = int(n)
        return (n*(1+n))/2
    except:
        n = int(n)
        return (n*(1+n))/2


def gcd(a, b):
    """find GCD/GCF of two numbers by Euclid’s GCD algorithm

    Arguments:
    - `a`: first number
    - `b`: second number
    """
    while a != 0:
        a, b = b % a, a
    return b    



