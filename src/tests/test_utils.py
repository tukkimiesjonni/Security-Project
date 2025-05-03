"""Unittests for testing utils module."""

import unittest
from util_functions.utils import (
    generate_bit,
    compute_phi,
    gen_prime_candidate,
    miller_rabin,
    generate_prime,
    generate_prime_pair
)


class TestKeyGenerationUtils(unittest.TestCase):
    """Unittest class"""

    def test_generate_bit_valid(self):
        """
        Test that generate_bit returns a valid integer within the specified bit length.

        Asserts that the generated bit is an integer, its bit length is less than or equal
        to the specified bit length, and it is greater than or equal to the lower bound
        for the bit length.
        """

        bit_length = 16
        result = generate_bit(bit_length)
        self.assertIsInstance(result, int)
        self.assertTrue(result.bit_length() <= bit_length)
        self.assertGreaterEqual(result, 2 ** (bit_length - 1) + 1)


    def test_generate_bit_invalid_type(self):
        """
        Test that generate_bit raises a TypeError when the bit length is not an integer.

        Ensures that the function raises the appropriate error when provided with
        a non-integer argument.
        """

        with self.assertRaises(TypeError):
            generate_bit("16")


    def test_generate_bit_invalid_value(self):
        """
        Test that generate_bit raises a ValueError when the bit length is less than 8.

        Ensures that the function enforces the constraint that the bit length must
        be at least 8, raising an appropriate error when violated.
        """

        with self.assertRaises(ValueError):
            generate_bit(4)


    def test_compute_phi(self):
        """
        Test the computation of Euler's totient function.

        Asserts that the function correctly computes the totient φ(n) for two prime numbers p and q.
        """

        p, q = 11, 13
        self.assertEqual(compute_phi(p, q), 120)


    def test_gen_prime_candidate_returns_valid_candidate(self):
        """
        Test that gen_prime_candidate returns a valid prime candidate.

        Asserts that the generated prime candidate is an integer and falls within
        the expected range for the specified bit length.
        """

        bit_length = 16
        candidate = gen_prime_candidate(bit_length)
        self.assertIsInstance(candidate, int)
        self.assertGreaterEqual(candidate, 2 ** (bit_length - 1))


    def test_miller_rabin_identifies_composite(self):
        """
        Test that the Miller-Rabin primality test correctly identifies a composite number.

        Asserts that the Miller-Rabin test returns False for a known composite number (100).
        """

        self.assertFalse(miller_rabin(100))


    def test_miller_rabin_identifies_prime(self):
        """
        Test that the Miller-Rabin primality test correctly identifies a prime number.

        Asserts that the Miller-Rabin test returns True for a known prime number (101).
        """

        self.assertTrue(miller_rabin(101))


    def test_generate_prime_returns_prime(self):
        """
        Test that generate_prime returns a prime number.

        Asserts that the function correctly generates a prime number and verifies it
        with the Miller-Rabin test.
        """

        prime = generate_prime(16)
        self.assertTrue(miller_rabin(prime))


    def test_generate_prime_pair_valid_output(self):
        """
        Test that generate_prime_pair returns valid prime numbers and correct modulus.

        Asserts that the two generated primes are valid, their product matches the expected modulus,
        and the modulus has the correct bit length.
        """

        p, q, n = generate_prime_pair(8, 16)
        self.assertTrue(miller_rabin(p))
        self.assertTrue(miller_rabin(q))
        self.assertEqual(n, p * q)
        self.assertEqual(n.bit_length(), 16)

if __name__ == "__main__":
    unittest.main()
