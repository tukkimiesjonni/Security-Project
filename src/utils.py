"""Importing random to produce random numbers."""

import random


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
