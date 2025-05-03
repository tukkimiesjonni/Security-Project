# Implementation Document

## 1. General Structure of the Program

The RSA encryption program is organized into five main modules, each responsible for a specific part of the overall functionality.

### • `main.py`
Serves as the user-facing entry point of the application. It handles user interaction via a terminal interface, displays the program logo, prompts for input (such as messages and key sizes), and calls the appropriate encryption or decryption functions. It also displays the resulting keys and messages in a formatted way.

### • `utils.py`
Contains utility functions essential to RSA key generation, such as:
- Generating random n-bit numbers
- Producing prime candidates
- Performing primality testing using the Miller-Rabin algorithm

### • `key_generation.py`
Handles the generation of RSA key pairs. It uses functions from `utils.py` to generate two large primes, compute the modulus and Euler’s totient, and calculate the modular inverse of the public exponent to form the private key. This module abstracts the cryptographic logic behind key creation.

### • `encryption.py`
Implements the RSA encryption process. It validates user input, converts the plaintext string into an integer, checks if it can be safely encrypted with the current key size, and then performs modular exponentiation using the public key.

### • `decryption.py`
Implements the RSA decryption process. It takes the ciphertext, performs modular exponentiation using the private key, and converts the resulting integer back into a UTF-8 string.

### • `primes.py`
A supplementary file that stores a precomputed list of small prime numbers. These are used in the initial filtering step of prime candidate generation to quickly eliminate obvious non-primes before applying more expensive primality tests.


## 2. Achieved Time and Space Complexities

Below is a summary of the key time and space complexities of the most computationally significant components:

### Miller-Rabin Primality Test
This algorithm is used to determine if a generated prime candidate is likely a prime. For a candidate number `n` and `k` rounds (trials), the time complexity is:

- **Time Complexity:** O(k × (log n)³)  
  Where k is the number of trials and n is the input number.

- **Space Complexity:** O(1)  
  The algorithm operates in constant space.

### Key Generation
RSA key generation involves creating two large prime numbers, computing a modulus `n = p × q`, and calculating a private exponent via modular inverse:

- **Time Complexity:** Dominated by primality testing → O(k × (log n)³) per prime, done twice (for `p` and `q`).
- **Space Complexity:** O(1) for each prime, as only integer variables are used.

### Encryption & Decryption
Both operations rely on modular exponentiation of integers:

- **Time Complexity:** O((log n)³) per operation.
- **Space Complexity:** O(1), with the result fitting into standard integer memory due to Python's arbitrary precision.


## 3. Performance and Complexity Comparison *(if applicable)*

## 4. Potential Shortcomings and Suggestions for Improvement

---

## 5. Use of Large Language Models

Throughout the project, I used various large language models such as GPT-4o Mini and Microsoft Copilot Chat (powered by GPT-4o) to rewrite documentation in a clearer form, as English is not my first language. This significantly sped up the writing of weekly reports.

## 6. Sources

[RSA Cryptosystem](https://en.wikipedia.org/wiki/RSA_cryptosystem)

[Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#)

[Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)

