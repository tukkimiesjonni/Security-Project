def decrypt(ciphertext: int, d: int, n: int):
    """Decrypts an integer ciphertext using RSA private key (d, n)."""
    decrypted_int = pow(ciphertext, d, n)  # Decrypt: m = c^d mod n
    decrypted_message = decrypted_int.to_bytes((decrypted_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return decrypted_message