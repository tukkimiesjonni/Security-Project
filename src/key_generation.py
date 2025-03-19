"""Importing random to produce large, random 1024 bit numbers 
   and Miller Rabin Algorithm to find 2 large primes"""

import random
from utils import miller_rabin

# Avainparin pitää olla 2048 bittiä pitkä
# Avain 1024 bittiä pitkä
# 309 desimaalia per avain

# Avainten luonti

# https://en.wikipedia.org/wiki/RSA_(cryptosystem)

def compute_primes():
    """Function that returns 1024 bit numbers that are prime according to Miller Rabin Algorithm"""

    found_primes = []

    while len(found_primes) < 2:
        test_number = random.getrandbits(1024) | 1
        if miller_rabin(test_number, 10) is True:
            if test_number not in found_primes:
                found_primes.append(test_number)

    return found_primes


def compute_modulus(found_primes: list):
    """Function that takes list of 2 primes as input and returns their multiplication"""

    modulus = found_primes[0] * found_primes[1]

    return modulus
