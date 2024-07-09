"""
Password checker

This script checks the strength of a password based on the following criteria:
- Length: Minimum 10 characters
- Contains at least one digit, uppercase letter, lowercase letter, and special character
- Not in a common password dictionary (rockyou.txt)

Gemukii
"""
import re

# Load the password dictionary
def load_password_dictionary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return set(file.read().splitlines())
    except FileNotFound:
        print(f"Error: Password dictionary file '{file_path}' not found.")
        return set()
        
# Path to password dictionary file
password_dictionary_file = 'rockyou.txt'

# Load the password dictionary file
common_passwords = load_password_dictionary(password_dictionary_file)

# Function to check the password strength
def check_password(password):
    length = len(password) >= 10
    digital = re.search(r'\d', password) is not None
    uppercase = re.search(r'[A-Z]', password) is not None
    lowercase = re.search(r'[a-z]', password) is not None
    special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    common_password = password.lower() not in common_passwords

# Strength level 
    if length and digital and uppercase and lowercase and special_char and common_password:
        return "Strong"
    elif length and (digital or special_char) and (uppercase or lowercase):
        return "Moderate"
    else:
        return "Weak"

# Function to print color
def color(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    color_code = colors.get(color.lower(), colors['end'])
    print(f"{color_code}{text}{colors['end']}")

# input pass to test
if __name__ == "__main__":
    try:
        password = input("Enter a password to check: ")
        strength = check_password(password)
        
# Print level this color 
        if strength == "Strong":
            color(f"The password is: {strength}", 'green')
        elif strength == "Moderate":
            color(f"The password  is: {strength}", 'yellow')
        else:
            color(f"The password  is: {strength}", 'red')
            
# Exception            
    except KeyboardInterrupt:
        print("\nPassword checking interrupted.")
