import random

def caesar_enc(s, k):
    s = list(s)
    s_enc = []
    for i in s:
        i = ord(i)
        i += int(k)
        if i >= 65536:
            i -= 65536
        i = chr(i)
        s_enc.append(i)
    return ''.join(s_enc)


def caesar_dec(s):
    s = list(s)
    s_dec = []
    symb = max(set(s), key = s.count)
    exp_k = ord(symb) - ord(' ')
    for i in s:
        i = ord(i)
        i -= int(exp_k)
        if i < 0:
            i += 65336
        i = chr(i)
        s_dec.append(i)
    return ''.join(s_dec)


def vernam_enc(s, k):
    s = list(s)
    k = list(k)
    count = 0
    s_enc = []
    for i in s:
        if k == '':
            k = list(input('Ключ не найден. Введите ключ: '))
            k = k[(count % len(k))]
        k = k[(count % len(k))]
        i = ord(i)
        i += ord(k)
        i = chr(i)
        count += 1
        s_enc.append(i)
    return ''.join(s_enc)


s = input('Введите текст для Цезаря: ')
k = random.randint(0, 65536)
s_enc = caesar_enc(s, k)
print(s_enc)
print(caesar_dec(s_enc))

sv = input('Введите текст для Вернама: ')
kv = input('Введите послед.ключей для Вернама: ')
print(vernam_enc(sv, kv))