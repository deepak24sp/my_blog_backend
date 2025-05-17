import hashlib
import os

def hash_password(password: str, salt: bytes = None):
    if not salt:
        salt = os.urandom(16)
    salt_hex = salt.hex()
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    return hashed.hex(), salt_hex
