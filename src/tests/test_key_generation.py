"""Import unittest and key_generation functions for testing purposes"""
import unittest
from src.utils import miller_rabin, gcd
from src.key_generation import compute_primes, compute_modulus, carmichael_lambda, compute_public_exponent

class TestKeyGeneration(unittest.TestCase):
    """Container for tests"""

    def test_compute_primes(self):
        """Ensure that gcd function returns correct values"""
        primes = compute_primes(10)
        self.assertEqual(len(primes), 2)
        self.assertTrue(miller_rabin(primes[0], 10))
        self.assertTrue(miller_rabin(primes[1], 10))
        self.assertNotEqual(primes[0], primes[1])


    def test_compute_modulus(self):
        """Ensure that compute_modulus function returns correct values"""
        primes = [3, 11]
        self.assertEqual(compute_modulus(primes), 33)


    def test_carmichael_lambda(self):
        """Ensure that carmichael_lambda function returns correct values"""
        self.assertEqual(carmichael_lambda(9), 6)
        self.assertEqual(carmichael_lambda(15), 4)
        self.assertEqual(carmichael_lambda(21), 6)
        self.assertEqual(carmichael_lambda(1), 1)


    def test_compute_public_exponent(self):
        """Ensure that compute_public_exponent function returns correct values"""
        modulus = 55
        exponent = compute_public_exponent(modulus)
        self.assertGreater(exponent, 1)
        self.assertLess(exponent, modulus)
        self.assertEqual(gcd(exponent, modulus), 1)

    # Might need to test with larger values.

if __name__ == '__main__':
    unittest.main()
    