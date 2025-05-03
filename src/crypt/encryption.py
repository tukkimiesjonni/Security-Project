"""Module for the encrypt function."""

def encrypt(message: str, public_key: tuple[int, int]) -> int:
    """
    Encrypt a UTF-8 encoded string using RSA public key encryption.

    This function converts a plaintext message to an integer and encrypts it using the RSA 
    encryption formula: ciphertext = message^e mod n.

    Args:
        message (str): The plaintext message to encrypt. Must be a non-empty UTF-8 string.
        public_key (tuple[int, int]): The RSA public key as a tuple (e, n), where:
            - e (int): The public exponent.
            - n (int): The RSA modulus.

    Returns:
        int: The encrypted message as an integer (ciphertext).

    Raises:
        TypeError: If the message is not a string or the public key is not a valid tuple of integers.
        ValueError: If the message is too long to encrypt with the given key size.
        ValueError: If the message is empty.
    """

    if not isinstance(message, str):
        raise TypeError("Input must be string.")

    if not message:
        raise ValueError("Input cannot be empty.")

    e, n = public_key
    msg_int = int.from_bytes(message.encode('utf-8'), 'big')

    if msg_int >= n:
        raise ValueError("Message is too long to encrypt with given bit length.")

    return pow(msg_int, e, n)
