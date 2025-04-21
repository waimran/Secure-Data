from cryptography.fernet import Fernet

# Generate and save a key
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Encrypt a message
message = b"Secret message"
encrypted = fernet.encrypt(message)
print("Encrypted:", encrypted)

# Decrypt it back
decrypted = fernet.decrypt(encrypted)
print("Decrypted:", decrypted.decode())
