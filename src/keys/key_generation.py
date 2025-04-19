"""Module for generating RSA keys."""

from util_functions.utils import compute_phi, generate_prime_pair


def generate_keys(bits: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Generate a pair of RSA keys (public and private)."""

    e = 65537

    while True:
        p, q, n = generate_prime_pair(bits // 2, bits)
        phi = compute_phi(p, q)

        if phi % e != 0:
            break

    d = pow(e, -1, phi)
    return (e, n), (d, n)
