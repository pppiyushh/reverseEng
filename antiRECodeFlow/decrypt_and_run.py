from utils import decrypt_data, hash_password
import sys

password = input("Enter password: ").strip()

with open("stored_password_hash.txt", "r") as f:
    stored_hash = f.read().strip()

if hash_password(password) != stored_hash:
    print("Auth failed.")
    sys.exit(1)

with open("payload/encrypted_payload.bin", "rb") as f:
    encrypted = f.read()

try:
    decrypted = decrypt_data(encrypted, password)
    exec(decrypted.decode(), globals())
except Exception as e:
    print("Decryption failed or code is invalid:", e)
