"""Main module for handling the process."""

from crypt.encryption import encrypt
from crypt.decryption import decrypt
from keys.key_generation import generate_keys
import pyfiglet


def logo() -> str:
    """
    Generate the ASCII art logo for the RSA terminal application.

    Uses the pyfiglet library to render a stylized banner.

    Returns:
        str: A string representing the ASCII art title.
    """

    return pyfiglet.figlet_format("RSA Machine", font="slant")


def display_menu() -> None:
    """
    Display the main menu for the RSA application in the terminal.

    Prints a formatted list of available options for the user.
    """

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
    """
    Run the main loop for the RSA terminal-based encryption application.

    Handles the following user operations:
    - Displays a banner and menu.
    - Allows encryption of messages with a generated public key.
    - Allows decryption of messages using the corresponding private key.
    - Manages input validation and key lifecycle.

    The loop runs until the user exits the program manually.
    """

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
