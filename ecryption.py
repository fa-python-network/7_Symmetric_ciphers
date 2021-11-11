from collections import Counter
from random import randint
N = 65536


def encrypt_caesar(k, m):
    offset_ords = [(x + k)%N for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def decrypt_caesar(k, m):
    offset_ords = [(x - k)%N for x in map(ord, m)]
    return ''.join(map(chr, offset_ords))


def hack(m):
    most_common = Counter(m).most_common()[0][0]
    key = ord(most_common) - ord(' ')
    return decrypt_caesar(key, m)


# шифр вернама
def generate_key(length):
    return [randint(0,26) for _ in range(length)]

def xor(char, key):
    return chr(ord(char)^key)

def encrypt_v(text):
    key = generate_key(len(text))
    return ''.join([xor(text[i], key[i]) for i in range(len(text))]), key

def decrypt_v(cryptedtext, key):
    return ''.join([xor(cryptedtext[i], key[i]) for i in range(len(cryptedtext))])

TEXT_TO_CHECK = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

key = int(input('Введите ключ для Цезаря: '))
text = encrypt_caesar(key, TEXT_TO_CHECK)
print('Зашифрованный текст Цезаря:', text)
print('---------------------------------------------------------------------------')
print('Расшифрованный текст Цезаря:', decrypt_caesar(key, text))
print('-----------------------------------------------------------------------------')
print('Взломанный текст Цезаря:', hack(text))
print('------------------------------------------------------------------------------')
encrypt_v, key = encrypt_v(TEXT_TO_CHECK)
print('Зашифрованный шифром Вернама текст: ', encrypt_v)
print('------------------------------------------------------------------------------')
decrypt_v = decrypt_v(encrypt_v, key)
print('Расшифрованный текст: ', decrypt_v)
print('------------------------------------------------------------------------------')