from random import randint


def block_encrypt(a1, key):
    a2 = [chr(ord(a1[i]) + ord(key[i])) for i in range(len(a1))]
    return a2


def block_decrypt(a1, key):
    a2 = [chr((ord(a1[i]) - ord(key[i]))) for i in range(len(a1))]
    return a2


def encrypt(str, key, iv):
    key_len = len(key)
    a1 = [i for i in str]
    a2 = []
    block = [i for i in iv]
    while a1 != []:
        a3 = [chr(ord(block[i]) ^ ord(a1[i])) for i in range(len(a1[:key_len]))]
        a2.extend(block_encrypt(a3, key))
        block = a2[-key_len:]
        a1 = a1[key_len:]
    return iv + ''.join(a2)


def decrypt(str, key):
    key_len = len(key)
    a1 = [i for i in str]
    a2 = []
    block = a1[:key_len]
    a1 = a1[key_len:]
    while a1 != []:
        a3 = block_decrypt(a1[:key_len], key)
        a2.extend([chr(ord(a3[i]) ^ ord(block[i])) for i in range(len(a3))])
        block = a1[:key_len]
        a1 = a1[key_len:]
    return ''.join(a2)


msg = 'Guess who\'s back, back again'
key = 'password'
iv = ''.join([chr(randint(1, 256)) for i in range(len(key))])
print(iv)
en_msg = encrypt(msg, key, iv)
de_msg = decrypt(en_msg, key)
print(en_msg)
print()
print(de_msg) 
