"""Unittests for testing encryption module"""

from crypt.encryption import encrypt
import pytest

VALID_PUBLIC_KEY = (65537, 2**1024)


def test_encrypt_valid_message():
    """
    Test that encrypting a valid UTF-8 string returns a positive integer ciphertext.

    Ensures the returned value is an integer and greater than zero, which indicates
    successful RSA encryption.
    """

    message = "Hello RSA"
    ciphertext = encrypt(message, VALID_PUBLIC_KEY)
    assert isinstance(ciphertext, int)
    assert ciphertext > 0


def test_encrypt_empty_message_raises_value_error():
    """
    Test that encrypting an empty string raises a ValueError.

    The function is expected to validate input and reject empty strings with an appropriate
    error message.
    """

    with pytest.raises(ValueError, match="Input cannot be empty."):
        encrypt("", VALID_PUBLIC_KEY)


def test_encrypt_non_string_input_raises_type_error():
    """
    Test that encrypting a non-string input raises a TypeError.

    This ensures type-checking is enforced and the function rejects non-string inputs like integers.
    """

    with pytest.raises(TypeError, match="Input must be string."):
        encrypt(1234, VALID_PUBLIC_KEY)


def test_encrypt_message_too_large_for_key_raises_value_error():
    """
    Test that encrypting a message too large for the RSA modulus raises a ValueError.

    This checks that the function prevents encryption of messages whose byte-encoded
    integer value exceeds the RSA modulus `n`.
    """

    oversized_message = "A" * 500
    small_n_key = (65537, 2**64)

    with pytest.raises(ValueError, match="Message is too long to encrypt"):
        encrypt(oversized_message, small_n_key)
