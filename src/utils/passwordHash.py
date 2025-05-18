import hashlib
import os
import hmac

def hash_password(password: str, salt: bytes = None):
    if not salt:
        salt = os.urandom(16)
    salt_hex = salt.hex()
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    return hashed.hex(), salt_hex

def verify_password(password, stored_hash, stored_salt):
    salt = bytes.fromhex(stored_salt)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hmac.compare_digest(hashed.hex(), stored_hash)