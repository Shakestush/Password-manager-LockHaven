import random
import string

def generate_password(length=16, include_uppercase=True, include_digits=True, 
                     include_special=True, exclude_similar=True):
    """Generate a strong random password"""
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if exclude_similar:
        for similar in "l1IoO0":
            chars = chars.replace(similar, "")
    
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        # Ensure password meets complexity requirements
        if (not include_uppercase or any(c.isupper() for c in password)) and \
           (not include_digits or any(c.isdigit() for c in password)) and \
           (not include_special or any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)):
            return password
