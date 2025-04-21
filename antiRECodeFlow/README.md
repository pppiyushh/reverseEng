# 🔐 Secure Local Application: Anti-Reverse Engineering Demo

This repo demonstrates how to protect local application logic using password hashing and symmetric encryption. The logic is encrypted and can only be decrypted and executed with the correct password.

## How it works
- `encrypt_payload.py` encrypts your logic using AES-GCM + scrypt key derivation.
- `decrypt_and_run.py` prompts the user for a password, verifies it, and decrypts the logic on the fly.

## Requirements
- Python 3.x
- `pycryptodome` (`pip install pycryptodome`)

## Usage

```bash
# Step 1: Encrypt your logic
python encrypt_payload.py

# Step 2: Run the protected app
python decrypt_and_run.py
```

## Disclaimer
This is a demo for educational purposes. In real-world applications, consider additional protection like anti-debugging, obfuscation, and memory management.
