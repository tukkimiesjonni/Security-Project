"""Import unittest and utils functions for testing purposes"""
import unittest
from src.utils import miller_rabin, sieve_of_eratosthenes, gcd, lcm, prime_factors

class TestUtils(unittest.TestCase):
    """Container for tests"""

    def test_gcd(self):
        """Ensure that gcd function returns correct values"""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 103), 1)
        self.assertEqual(gcd(56, 98), 14)
        self.assertEqual(gcd(10, 5), 5)
        self.assertEqual(gcd(7, 1), 1)

    def test_lcm(self):
        """Ensure that lcm function returns correct values"""
        self.assertEqual(lcm(4, 5), 20)
        self.assertEqual(lcm(6, 8), 24)
        self.assertEqual(lcm(7, 3), 21)
        self.assertEqual(lcm(10, 5), 10)
        self.assertEqual(lcm(1, 1), 1)


    def test_prime_factors(self):
        """Ensure that prime_factors function returns correct values"""
        self.assertEqual(prime_factors(60), {2: 2, 3: 1, 5: 1})
        self.assertEqual(prime_factors(13), {13: 1})
        self.assertEqual(prime_factors(100), {2: 2, 5: 2})
        self.assertEqual(prime_factors(1), {})
        self.assertEqual(prime_factors(37), {37: 1})
        self.assertEqual(prime_factors(84), {2: 2, 3: 1, 7: 1})


    def test_miller_rabin(self):
        """Ensure that miller_rabin function returns correct values"""
        self.assertTrue(miller_rabin(7, 5))
        self.assertTrue(miller_rabin(13, 5))
        self.assertTrue(miller_rabin(209669, 5))
        self.assertTrue(miller_rabin(99999997351, 5))
        self.assertFalse(miller_rabin(9, 5))
        self.assertFalse(miller_rabin(100, 5))
        self.assertFalse(miller_rabin(1, 5))
        self.assertFalse(miller_rabin(99999997350, 5))


    def test_sieve_of_erastothenes(self):
        """Ensure that sieve_of_erastothenes function returns correct values"""
        self.assertEqual(sieve_of_eratosthenes(10), [2, 3, 5, 7])
        self.assertEqual(sieve_of_eratosthenes(2), [2])
        self.assertEqual(sieve_of_eratosthenes(1), [])
        self.assertEqual(sieve_of_eratosthenes(0), [])
        self.assertEqual(sieve_of_eratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    # Might need to write tests for larger values also

if __name__ == '__main__':
    unittest.main()
    