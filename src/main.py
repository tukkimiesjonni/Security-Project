"""Importing pyfiglet for nice ASCII art"""

import pyfiglet


def logo():
    """Function to print logo for the application"""

    text = "RSA Machine"
    figlet = pyfiglet.figlet_format(text, font='slant')

    return figlet


def main():
    """Main function to run the terminal application"""

    print(logo())

    lines = [
        "|| ** This is a program for encrypting and decrypting messages using RSA",
        "||",
        "|| 1. Encrypt message",
        "|| 2. Decrypt message"
    ]

    max_length = max(len(line) for line in lines)

    for line in lines:
        print(line.ljust(max_length) + " ||")

    print("||".ljust(max_length) + " ||")

    while True:
        selection = input("|| ** Please select a mode".ljust(max_length) + " ||\n")

        if selection == "1":
            plaintext_string = input("|| ** Input string to encrypt".ljust(max_length) + " ||\n")
            # Insert input string here
            # Input key bit length
            # Run encrypting functions
            # Run key generation functions
            # Print key
            # Print encrypted message
        elif selection == "2":
            encrypted_string = input("|| ** Input string to decrypt".ljust(max_length) + " ||\n")
            # Insert encrypted string
            # Insert key
            # Run decrypting functions
            # Print decrypted string
        else:
            # Bad input, request new input
            print("|| ** Please enter a valid number".ljust(max_length) + " ||\n")


if __name__ == "__main__":
    main()
