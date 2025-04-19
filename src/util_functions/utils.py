"""Module for all other functions that are needed in key generation."""

import random
from util_functions import primes


def generate_bit(bit_length: int) -> int:
    """Generate a random integer with the specified bit length."""

    if not isinstance(bit_length, int):
        raise TypeError("Bit length must be an integer.")

    if bit_length < 8:
        raise ValueError(f"Bit length must be at least 8. Got {bit_length}.")

    lower_bound = 2 ** (bit_length - 1) + 1
    upper_bound = 2 ** bit_length - 1
    return random.SystemRandom().randint(lower_bound, upper_bound)


def compute_phi(p: int, q: int) -> int:
    """Compute Euler's totient function."""

    return (p - 1) * (q - 1)


def generate_prime_pair(bits: int, expected_bits: int) -> tuple[int, int, int]:
    """Generate two primes such that their product has the expected bit length."""

    while True:
        p = generate_prime(bits)
        q = generate_prime(bits)
        n = p * q
        if n.bit_length() == expected_bits:
            return p, q, n


def gen_prime_candidate(bit_length: int) -> int:
    """Generate a candidate prime number of the given bit length."""

    while True:
        candidate = generate_bit(bit_length)
        if all(candidate % d != 0 or d**2 > candidate for d in primes.primes):
            return candidate


def miller_rabin(candidate: int, trials: int = 20) -> bool:
    """Perform the Miller-Rabin primality test."""

    if candidate % 2 == 0:
        return False

    r, d = 0, candidate - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    def is_composite(a: int) -> bool:
        if pow(a, d, candidate) == 1:
            return False
        return all(pow(a, 2**i * d, candidate) != candidate - 1 for i in range(r))

    rand_gen = random.SystemRandom()
    for _ in range(trials):
        a = rand_gen.randint(2, candidate - 2)
        if is_composite(a):
            return False
    return True


def generate_prime(bit_length: int) -> int:
    """Generate a prime number of the specified bit length."""

    while True:
        candidate = gen_prime_candidate(bit_length)
        if miller_rabin(candidate):
            return candidate
