#2nd Practical
def encrypt(plaintext, key):
    columns = [""] * key
    for i, char in enumerate(plaintext):
        columns[i % key] += char
    return "".join(columns)

def decrypt(ciphertext, key):
    rows = len(ciphertext) // key
    columns = len(ciphertext) // rows
    last_column_len = len(ciphertext) % columns
    plaintext = [""] * columns
    column = 0
    row = 0
    for char in ciphertext:
        plaintext[column] += char
        column += 1
        if (column == columns) or (column == last_column_len and row >= rows - 1):
            column = 0
            row += 1
    return "".join(plaintext)

plaintext = "secret message"
key = 4

ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
