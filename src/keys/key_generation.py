"""Module for generating RSA keys."""

from util_functions.utils import compute_phi, generate_prime_pair


def generate_keys(bits: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Generate a pair of RSA keys (public and private) with the specified bit length.

    This function generates two large prime numbers `p` and `q` such that their product `n` has 
    the desired bit length. It then calculates the RSA modulus `n`, the public exponent `e` 
    (commonly 65537), and the private exponent `d` such that `d` is the modular inverse of `e` modulo φ(n),
    where φ(n) = (p - 1) * (q - 1).

    Args:
        bits (int): The desired total bit length of the RSA modulus `n`. Must be at least 8.

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: A tuple containing:
            - The public key as a tuple (e, n)
            - The private key as a tuple (d, n)

    Raises:
        ValueError: If valid primes satisfying the bit length requirements cannot be generated.
    """
    
    e = 65537

    while True:
        p, q, n = generate_prime_pair(bits // 2, bits)
        phi = compute_phi(p, q)

        if phi % e != 0:
            break

    d = pow(e, -1, phi)
    return (e, n), (d, n)
