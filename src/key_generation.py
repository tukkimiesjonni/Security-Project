"""Importing random to generate random values,
   Importing different helper functions from utils
   to compute required values for generating the keys"""

import random
from src.utils import miller_rabin, lcm, gcd, prime_factors

# Avainparin pitää olla 2048 bittiä pitkä
# Avain 1024 bittiä pitkä
# 309 desimaalia per avain

# Avainten luonti

# https://en.wikipedia.org/wiki/RSA_(cryptosystem)

def compute_primes(bit_length: int):
    """Function that returns user determined bit length numbers that are prime"""

    found_primes = []

    while len(found_primes) < 2:
        test_number = random.getrandbits(bit_length) | 1
        if miller_rabin(test_number, 10) is True:
            if test_number not in found_primes:
                found_primes.append(test_number)

    return found_primes


def compute_modulus(found_primes: list):
    """Function that takes list of 2 primes as input and returns their multiplication"""

    modulus = found_primes[0] * found_primes[1]

    return modulus

def carmichael_lambda(n):
    """Computes the Carmichael function λ(n)."""
    if n == 1:
        return 1

    factors = prime_factors(n)
    lambdas = []

    for p, k in factors.items():
        if p == 2:
            if k == 1:
                lambdas.append(1)
            elif k == 2:
                lambdas.append(2)
            else:
                lambdas.append(2 ** (k - 2))
        else:
            lambdas.append((p - 1) * p ** (k - 1))

    result = lambdas[0]
    for value in lambdas[1:]:
        result = lcm(result, value)

    return result

# ***** I think this works *****
# MUST BE REFACTORED

def compute_public_exponent(modulus: int):
    """Computes public exponent from range 1 < e < mod and ensures that e and mod are coprime"""

    while True:
        exponent = random.randrange(1, modulus)
        if gcd(exponent, modulus) == 1:
            break

    return exponent

    # Might need to optimize finding e...
    # e having a short bit-length and small Hamming weight results in more efficient encryption – 
    # the most commonly chosen value for e is 216 + 1 = 65537. The smallest (and fastest) 
    # possible value for e is 3, but such a small value for e has been shown to be less secure in some settings
