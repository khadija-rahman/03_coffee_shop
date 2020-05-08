# Import Package
from cryptography.fernet import Fernet

# Generate a Key and Instantiate a Fernet Instance
key = Fernet.generate_key()
f = Fernet(key)
print(key)

# Define our message
plaintext = b'encrypting is just as useful'

# Encrypt
ciphertext = f.encrypt(plaintext)
print(ciphertext)

# # Decrypt
# decryptedtext = f.decrypt(ciphertext)
# print(decryptedtext)