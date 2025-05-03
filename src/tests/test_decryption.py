"""Unittests for decryption module."""

from crypt.decryption import decrypt
from crypt.encryption import encrypt
import pytest


PUBLIC_KEY = (65537, 3233)    # e, n
PRIVATE_KEY = (2753, 3233)    # d, n


def test_decrypt_valid_ciphertext():
    """
    Test that decrypting a valid RSA-encrypted ciphertext returns the original message.

    This ensures the decryption process correctly inverts the RSA encryption,
    given matching key pairs and valid input.
    """

    message = "A"
    ciphertext = encrypt(message, PUBLIC_KEY)
    decrypted = decrypt(ciphertext, PRIVATE_KEY)
    assert decrypted == message


def test_decrypt_non_integer_ciphertext_raises_type_error():
    """
    Test that passing a non-integer ciphertext to decrypt raises a TypeError.

    This confirms that the function enforces input type validation.
    """

    with pytest.raises(TypeError, match="Encrypted string must be an integer."):
        decrypt("not an int", PRIVATE_KEY)


def test_decrypt_with_invalid_utf8_bytes_raises_value_error():
    """
    Test that decryption resulting in invalid UTF-8 bytes raises a ValueError.

    This checks the robustness of the UTF-8 decoding step and ensures proper error handling
    when the decrypted integer does not map to a valid UTF-8 byte sequence.
    """

    bad_msg_int = int.from_bytes(b'\xff\xff\xff', 'big')
    forged_key = (1, bad_msg_int + 1)

    with pytest.raises(ValueError, match="Result can't be decoded."):
        decrypt(bad_msg_int, forged_key)
