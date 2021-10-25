from collections import Counter

N = 65536


def encrypt(k, m):
    och = [(x + k) % N for x in map(ord, m)]
    return ''.join(map(chr, och))


def decrypt(k, c):
    och = [(x - k) % N for x in map(ord, c)]
    return ''.join(map(chr, och))


def vz(m):
    most = Counter(m).most_common()[0][0]
    key = ord(most) - ord(' ')
    return decrypt(key, m)


def encrypt_ver(k, m):
    k = k * (len(m) // len(k)) + k[:(len(m) % len(k))]
    return ''.join(map(chr, [i ^ x for i, x in zip(map(ord, m), map(ord, k))]))


def decrypt_ver(k, c):
    return encrypt_ver(k, c)


k = int(input('Введите ключ для Цезаря: '))
text = "Говорят, после аварии ты ничего не помнишь о нас. Так почему же ты всегда находишь меня, несмотря на все мои " \
       "переезды? "
print("Текст: ", text)
za_text = encrypt(k, text)
de_text = decrypt(k, za_text)
print('Зашифрованный текст Цезаря:', za_text)
print('Расшифрованный текст Цезаря:', de_text)
print('Расшифрованный текст Цезаря(без знания ключа):', vz(za_text))
k = "1 2 5 4 9 8"
za_text_ver = encrypt_ver(k, text)
de_text_ver = decrypt_ver(k, za_text_ver)
print('Зашифрованный текст шифра Вернама:', za_text_ver)
print('Расшифрованный текст шифра Вернама:', de_text_ver)