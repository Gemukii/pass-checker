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
    sepcial_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    common_password = password.lower() not in common_passwords

# Strength level 
    if length_criteria and digit_criteria and uppercase_criteria and lowercase_criteria and special_char_criteria and common_password_criteria:
        return "Strong"
    elif length_criteria and (digit_criteria or special_char_criteria) and (uppercase_criteria or lowercase_criteria):
        return "Moderate"
    else:
        return "Weak"

# input pass to test
if __name__ == "__main__":
    try:
        password = input("Enter a password to check: ")
        strength = check_password_strength(password)
        print(f"The password strength is: {strength}")
    except KeyboardInterrupt:
        print("\nPassword checking interrupted.")
