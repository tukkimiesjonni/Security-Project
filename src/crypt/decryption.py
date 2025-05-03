"""Module for the decrypt function."""

def decrypt(ciphertext: int, private_key: tuple[int, int]) -> str:
    """
    Decrypt an RSA-encrypted integer back into a UTF-8 string using the private key.

    This function reverses RSA encryption by computing the modular exponentiation
    of the ciphertext with the private key components. The resulting integer is then
    converted back into a UTF-8 encoded string.

    Args:
        ciphertext (int): The RSA-encrypted message as an integer.
        private_key (tuple[int, int]): The RSA private key as a tuple (d, n), where:
            - d (int): The private exponent.
            - n (int): The RSA modulus.

    Returns:
        str: The decrypted plaintext message as a UTF-8 string.

    Raises:
        TypeError: If the ciphertext is not an integer or the private key is not a valid tuple.
        ValueError: If the decryption result cannot be decoded into a valid UTF-8 string.
    """

    if not isinstance(ciphertext, int):
        raise TypeError("Encrypted string must be an integer.")

    d, n = private_key

    msg_int = pow(ciphertext, d, n)

    try:
        return msg_int.to_bytes((msg_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    except Exception as e:
        raise ValueError("Result can't be decoded.") from e
