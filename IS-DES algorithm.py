#3rd Practical
import pyDes

data = "secret message"
key = "12345678"

k = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

encrypted_data = k.encrypt(data)
print("Encrypted: %r" % encrypted_data)

decrypted_data = k.decrypt(encrypted_data)
print("Decrypted: %r" % decrypted_data)
