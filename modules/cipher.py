import random
def xor_cipher( str, key ):
    encript_str = ""
    for letter in str:
        encript_str += chr(ord(letter)^key)
    return encript_str
def ciphergenkey():
    cipherkey = "1234567890"
    key = int(random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey) + random.choice(cipherkey))
    return key