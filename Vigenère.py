def encrypt(str, key):
    a1 = [i for i in str]
    a2 = [key[i % len(key)] for i in range(len(a1))]
    a3 = [chr((ord(a1[i]) + ord(a2[i]))) for i in range(len(a1))]
    return ''.join(a3)


def decrypt(str, key):
    a1 = [i for i in str]
    a2 = [key[i % len(key)] for i in range(len(a1))]
    a3 = [chr((ord(a1[i]) - ord(a2[i]))) for i in range(len(a1))]
    return ''.join(a3)


msg = '\'Til the roof comes off, till the lights go out'
key = 'password'
en_msg = encrypt(msg, key)
de_msg = decrypt(en_msg, key)
print(en_msg)
print(de_msg)
