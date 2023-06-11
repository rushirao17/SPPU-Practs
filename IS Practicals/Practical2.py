"""
Write a Java/C/C++/Python program to perform encryption and decryption using the method of Transposition technique.
"""
# Transposition Technique:

def encrypt(PT, key):
    CT = [""] * key
    for column in range(key):
        pointer = column
        while pointer < len(PT):
            CT[column] += PT[pointer]
            pointer += key
    return CT

def decrypt(e_text):
    key = len(e_text)
    PT_length = 0
    for i in e_text:
        PT_length += len(i)
        d_text = [""] * PT_length
        
    for column in range(key):
        pointer = column
        word = e_text[column]
        c = 0
        while pointer < PT_length:
            d_text[pointer] = word[c]
            pointer += key
            c += 1
    return d_text


PT = input ("type the message: ")
e_text = encrypt(PT, 3)
print("".join(e_text))

d_text = decrypt(e_text)
print("".join(d_text))
