"""Unittests for testing key_generation module."""

from keys.key_generation import generate_keys
import pytest


def test_generate_keys_returns_valid_key_structure():
    """
    Test that generate_keys returns a properly structured pair of keys.

    Asserts that the public and private keys are tuples of length 2,
    and all elements are integers.
    """

    public_key, private_key = generate_keys(16)

    assert isinstance(public_key, tuple)
    assert isinstance(private_key, tuple)
    assert len(public_key) == 2
    assert len(private_key) == 2
    assert all(isinstance(x, int) for x in public_key)
    assert all(isinstance(x, int) for x in private_key)


def test_public_and_private_keys_match_modulus():
    """
    Test that the public and private keys share the same RSA modulus.

    The modulus `n` must be identical in both keys for RSA to function correctly.
    """

    public_key, private_key = generate_keys(16)
    _, n1 = public_key
    _, n2 = private_key
    assert n1 == n2


def test_generate_keys_bit_length_accuracy():
    """
    Test that the generated RSA modulus has the correct bit length.

    Allows a ±1 bit tolerance due to binary rounding during prime multiplication.
    """

    bit_length = 16
    public_key, _ = generate_keys(bit_length)
    _, n = public_key
    assert abs(n.bit_length() - bit_length) <= 1


def test_generate_keys_rejects_small_bit_length():
    """
    Test that generate_keys raises a ValueError when given a bit length that's too small.

    Ensures that the function enforces a minimum bit length constraint.
    """

    with pytest.raises(ValueError):
        generate_keys(4)
