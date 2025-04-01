"""Importing pyfiglet for nice ASCII art, and other packages for functions"""
from crypt.encryption import encrypt
from crypt.decryption import decrypt
from keys.key_generation import compute_modulus, compute_primes, compute_private_exponent, compute_public_exponent, carmichael_lambda
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
            bit_length = int(input("|| Input desired bit length".ljust(max_length) + " ||\n"))
            primes = compute_primes(bit_length)
            modulus = compute_modulus(primes)
            carmichael_n = carmichael_lambda(modulus)
            public_exponent = compute_public_exponent(carmichael_n)
            private_exponent = compute_private_exponent(public_exponent, carmichael_n)

            print(f"Public Key: (n={carmichael_n}, e={public_exponent})".ljust(max_length) + " ||\n")
            print(f"Private Key: (n={carmichael_n}, d={private_exponent})".ljust(max_length) + " ||\n")
            print(f"Plaintext message: {plaintext_string}".ljust(max_length) + " ||\n")
            encrypted_string = encrypt(plaintext_string, public_exponent, modulus)
            print(f"Encrypted string: {encrypted_string}")
            # Insert input string here
            # Input key bit length
            # Run encrypting functions
            # Run key generation functions
            # Print key
            # Print encrypted message
        elif selection == "2":
            string_input = int(input("|| ** Input the encrypted integer: ").strip()) # Doesn't work wihtout strip()???
            decrypted_message = decrypt(string_input, private_exponent, modulus)
            print(f"Decrypted: {decrypted_message}")
            # encrypted_string = input("|| ** Input string to decrypt".ljust(max_length) + " ||\n")
            # Insert encrypted string
            # Insert key
            # Run decrypting functions
            # Print decrypted string
        else:
            # Bad input, request new input
            print("|| ** Please enter a valid number".ljust(max_length) + " ||\n")


if __name__ == "__main__":
    main()
