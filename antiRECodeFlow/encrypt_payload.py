from utils import encrypt_data, hash_password

with open("payload/secret_logic.py", "rb") as f:
    payload = f.read()

password = input("Set a password to encrypt the logic: ").strip()
enc = encrypt_data(payload, password)

with open("payload/encrypted_payload.bin", "wb") as f:
    f.write(enc)

with open("stored_password_hash.txt", "w") as f:
    f.write(hash_password(password))

print("Payload encrypted and saved.")
