"""Module for the decrypt function."""

def decrypt(ciphertext: int, private_key: tuple[int, int]) -> str:
    """Decrypt an RSA-encrypted integer back to a UTF-8 string using the private key."""

    d, n = private_key

    msg_int = pow(ciphertext, d, n)
    return msg_int.to_bytes((msg_int.bit_length() + 7) // 8, 'big').decode('utf-8')
