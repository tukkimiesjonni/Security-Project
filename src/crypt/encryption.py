"""Module for the encrypt function."""

def encrypt(message: str, public_key: tuple[int, int]) -> int:
    """Encrypt a UTF-8 encoded string using RSA public key encryption."""

    e, n = public_key
    msg_int = int.from_bytes(message.encode('utf-8'), 'big')

    return pow(msg_int, e, n)
