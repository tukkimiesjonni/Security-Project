def encrypt(message: str, e: int, n: int):
    """Encrypts a string message using RSA public key (e, n)."""
    message_int = int.from_bytes(message.encode('utf-8'), 'big')  # Convert string to integer
    ciphertext = pow(message_int, e, n)  # Encrypt: c = m^e mod n
    return ciphertext