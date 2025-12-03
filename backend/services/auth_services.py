import hashlib
import os

# Creating a class that can hash and verify passwords.

# Hash password when registering
class AuthService:
    @staticmethod
    def hash_password(password):
        salt = os.urandom(16)
        hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
        return salt.hex() + ":" + hashed.hex()
    
# Check password is correct.
    def verify_password(password, stored_hash):
        salt_hex, hash_hex = stored_hash.split(":")
        salt = bytes.fromhex(salt_hex)
        stored_hash_bytes = bytes.fromhex(hash_hex)

        new_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
        return new_hash == stored_hash_bytes