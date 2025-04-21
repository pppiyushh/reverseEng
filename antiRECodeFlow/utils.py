import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt

SCRYPT_N = 2**14
SCRYPT_R = 8
SCRYPT_P = 1
KEY_LEN = 32  # For AES-256

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def derive_key(password: str, salt: bytes) -> bytes:
    return scrypt(password.encode(), salt, KEY_LEN, N=SCRYPT_N, r=SCRYPT_R, p=SCRYPT_P)

def encrypt_data(data: bytes, password: str) -> bytes:
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return salt + cipher.nonce + tag + ciphertext

def decrypt_data(enc_data: bytes, password: str) -> bytes:
    salt = enc_data[:16]
    nonce = enc_data[16:32]
    tag = enc_data[32:48]
    ciphertext = enc_data[48:]
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
