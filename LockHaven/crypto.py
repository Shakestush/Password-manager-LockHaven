rom cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os

def generate_key(master_password: str, salt: bytes) -> bytes:
    """Derive encryption key from master password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

def encrypt_password(key: bytes, password: str) -> str:
    """Encrypt a password"""
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key: bytes, encrypted_password: str) -> str:
    """Decrypt a password"""
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()
