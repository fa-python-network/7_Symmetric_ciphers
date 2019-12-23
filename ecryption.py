import random 
iv = ord(chr(random.getrandbits(10)))

inp_string = "Yeah. Here we go again"
print("User string:" +  "{:>29}\n".format(inp_string))

def encrypt(key, inp_string):
    out_string = ""
    xor_encr = iv
    for i,s in enumerate(inp_string):
        xor_encr = ord(s) ^ xor_encr ^ ord(key[i % len(key)])
        out_string += chr(xor_encr)
    
    return out_string


def decrypt(key, inp_string):
    out_string = ""
    xor_dec = iv
    for i, s in enumerate(inp_string):
        out_string += chr(ord(s) ^ ord(key[i % len(key)]) ^ xor_dec)
        xor_dec = ord(s)
    
    return out_string


enc = encrypt('hello', inp_string)
print(f"Encrypted message: {enc}\n")

decr = decrypt('hello', enc)
print(f"Decrypted message: {decr}")