#4th Practical
from Crypto.Cipher import AES
import base64

key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'

def encrypt(plaintext, key, block_size=16):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = plaintext + (block_size - len(plaintext) % block_size) * chr(block_size - len(plaintext) % block_size)
    encrypted_data = cipher.encrypt(padded_plaintext.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt(encrypted_text, key, block_size=16):
    encrypted_text = base64.b64decode(encrypted_text.encode('utf-8'))
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_text).decode('utf-8')
    padding_length = decrypted_data[-1]
    return decrypted_data[:-padding_length]

plaintext = "secret message"

encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
