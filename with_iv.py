from random import randint


def block_incript(a1, key):
    a2 = [chr(ord(a1[i]) + ord(key[i])) for i in range(len(a1))]
    return a2


def block_decript(a1, key):
    a2 = [chr((ord(a1[i]) - ord(key[i]))) for i in range(len(a1))]
    return a2


def incript(st, key, iv):
    key_len = len(key)
    a1 = [i for i in st]
    a2 = []
    block = [i for i in iv]
    while a1 != []:
        a3 = [chr(ord(block[i]) ^ ord(a1[i])) for i in range(len(a1[:key_len]))]
        a2.extend(block_incript(a3, key))
        block = a2[-key_len:]
        a1 = a1[key_len:]
    return iv + ''.join(a2)


def decript(st, key):
    key_len = len(key)
    a1 = [i for i in st]
    a2 = []
    block = a1[:key_len]
    a1 = a1[key_len:]
    while a1 != []:
        a3 = block_decript(a1[:key_len], key)
        a2.extend([chr(ord(a3[i]) ^ ord(block[i])) for i in range(len(a3))])
        block = a1[:key_len]
        a1 = a1[key_len:]
    return ''.join(a2)


msg = 'hbfi jdbiwd, okdsnfio abcdefgнlo'
key = 'password'
iv = ''.join([chr(randint(1, 256)) for i in range(len(key))])
print(iv)
new_msg = incript(msg, key, iv)
new_new_msg = decript(new_msg, key)
print(new_msg)
print()
print(new_new_msg) 