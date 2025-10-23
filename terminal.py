import os

def clear():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')
