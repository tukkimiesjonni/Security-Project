"""Importing pyfiglet for nice ASCII art"""

import pyfiglet

def logo():
    """Function to print logo for the application"""

    text = "RSA Machine"
    figlet = pyfiglet.figlet_format(text, font='slant')

    return figlet
