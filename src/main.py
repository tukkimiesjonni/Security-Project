"""Main module for handling the process."""

from crypt.encryption import encrypt
from crypt.decryption import decrypt
from keys.key_generation import generate_keys
import pyfiglet


def logo() -> str:
    """Print logo for te terminal app."""

    return pyfiglet.figlet_format("RSA Machine", font="slant")


def display_menu() -> None:
    """Print the menu to the terminal."""

    menu_lines = [
        "|| ** This is a program for encrypting and decrypting messages using RSA",
        "||",
        "|| 1. Encrypt message",
        "|| 2. Decrypt message"
    ]
    max_length = max(len(line) for line in menu_lines)

    for line in menu_lines:
        print(line.ljust(max_length) + " ||")
    print("||".ljust(max_length) + " ||")


def main() -> None:
    """Main loop that handles mode selection and function calls."""

    print(logo())
    display_menu()

    private_key = None

    while True:
        selection = input("|| ** Please select a mode: ").strip()

        if selection == "1":
            message = input("|| ** Input string to encrypt: ").strip()
            try:
                bit_length = int(input("|| Input desired bit length: ").strip())
            except ValueError:
                print("|| ** Invalid bit length. Please enter a valid integer.")
                continue

            public_key, private_key = generate_keys(bit_length)

            print(f"Public Key: {public_key}")
            print(f"Private Key: {private_key}")
            print(f"Plaintext message: {message}")
            encrypted = encrypt(message, public_key)
            print(f"Encrypted string: {encrypted}")

        elif selection == "2":
            if not private_key:
                print("|| ** No private key available. Please encrypt a message first.")
                continue

            try:
                encrypted_input = int(input("|| ** Input the encrypted string: ").strip())
            except ValueError:
                print("|| ** Invalid input. Please enter a numeric ciphertext.")
                continue

            decrypted = decrypt(encrypted_input, private_key)
            print(f"Decrypted: {decrypted}")

        else:
            print("|| ** Please enter a valid number (1 or 2).")


if __name__ == "__main__":
    main()
