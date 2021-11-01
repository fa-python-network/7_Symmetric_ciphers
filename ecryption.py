import collections


# CAESAR
def encrypt(k, m):
    text = ''
    for x in m:
        a = ord(x)
        a = a + k
        if (a / 65537) < 1:
            text = text + chr(a)
        if (a / 65537) >= 1:
            print('Out of range 65536')
    return text


def decrypt(k, c):
    text = ''
    for x in c:
        a = ord(x)
        a = a - k
        if (a / 65537) < 1:
            text = text + chr(a)
        if (a / 65537) >= 1:
            print('Out of range 65536')
    return text


def smart_decrypt(с):
    results = collections.Counter(c)
    v = sorted(results, key=None, reverse=False)
    k = ord(v[0]) - ord(' ')
    print('Identified key:', k)
    return decrypt(k, c)


# VERNAM
def encrypt_v(k, m):
    k = k * (len(m) // len(k)) + k[:(len(m) % len(k))]
    return ''.join(map(chr, [i ^ x for i, x in zip(map(ord, m), map(ord, k))]))


def decrypt_v(k, c):
    return encrypt_v(k, c)


# COMMANDS
try:
    cipher = int(input(' 1. Caesar cipher\n 2. Vernam cipher\nEnter the number: '))
    choose = int(input('You want to:\n 1. Encrypt\n 2. Decrypt\nEnter the number: '))
    if cipher == 1:
        print('CAESAR')
        if choose == 1:
            m = input('Enter the text you want to encrypt: ')
            k = int(input('Enter the key: '))
            print('Encrypted text:', encrypt_v(k, m))
        if choose == 2:
            c = input('Enter the text you want to decrypt: ')
            dec = int(input('Do you know the key?\n 1. Yes\n 2. No\nEnter the number: '))
            if dec == 1:
                k = int(input('Enter the key: '))
                print('Decrypted text:', decrypt_v(k, c))
            if dec == 2:
                print('Decrypted text (without knowing the key):', smart_decrypt(c))
    if cipher == 2:
        print('VERNAM')
        if choose == 1:
            m = input('Enter the text you want to encrypt: ')
            k = input('Enter the keys (Example: 1 2 3 4): ')
            print('Encrypted text: ', encrypt_v(k, m))
        if choose == 2:
            c = input('Enter the text you want to decrypt: ')
            k = input('Enter the keys (Example: 1 2 3 4): ')
            print('Decrypted text: ', decrypt_v(k, c))
except ValueError or TypeError or NameError:
    print('Something went wrong. Try again')
