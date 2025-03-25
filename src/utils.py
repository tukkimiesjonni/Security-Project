"""Importing random and math to produce random numbers and to count gcd and lcm."""

import random
import math


def miller_rabin(n: int, k: int):
    """Function for checking if a number is prime"""

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            if x == 1:
                return False

        else:
            return False

    return True

# ***** I think this works *****

def sieve_of_eratosthenes(n: int):
    """Function for finding prime numbers"""

    if n < 2:
        return []

    bool_array = [True] * (n + 1)
    bool_array[0] = bool_array[1] = False

    for i in range(2, int(n**0.5) + 1):
        if bool_array[i]:
            for j in range(i * i, n + 1, i):
                bool_array[j] = False

    return [i for i, is_prime in enumerate(bool_array) if is_prime]

# ***** I think this works *****

def gcd(a, b):
    """Compute the greatest common divisor (GCD) using Euclidean algorithm."""
    return math.gcd(a,b)


def lcm(a, b):
    """Compute the least common multiple (LCM)"""
    return math.lcm(a,b)


def prime_factors(n):
    """Returns the prime factorization of n as a dictionary {p: k}."""
    i = 2
    factors = {}
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors
