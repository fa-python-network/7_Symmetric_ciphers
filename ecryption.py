from collections import Counter

# максимум для chr
mx = 65536


# зашифровка методом цезаря
def encrypt(k, m):
    return ''.join(map(chr, [(x + k) % mx for x in map(ord, m)]))


# расшифровка методом цезаря
def decrypt(k, c):
    return ''.join(map(chr, [(x - k) % mx for x in map(ord, c)]))


# разница в + и - чтобы добавить ключ в зашифровке и вычесть в расшифровке

# поиск чаще всего встречающегося элемента(зашифрованного пробела) и дешифровка
def decrypt_unknown(m):
    most = Counter(m).most_common()[0][0]
    # print(most)
    key = ord(most) - ord(' ')
    return decrypt(key, m)


# "размножение" ключа и xor в шифровании
def encrypt_(k, m):
    k = k * (len(m) // len(k)) + k[:(len(m) % len(k))]
    return ''.join(map(chr, [i ^ x for i, x in zip(map(ord, m), map(ord, k))]))


# дешифровка
def decrypt_(k, c):
    return encrypt_(k, c)


# сегмент проверки
a = encrypt(2, 'Окаери, докта! Мы ждали вашего возвращения. Как ваша память? Еще помните нас?')
b = encrypt(3, 'Окаери, докта! Мы ждали вашего возвращения.')

c = decrypt_unknown(a)
d = decrypt_unknown(b)

print('Работающая зашифровка зная ключ')
print(a, '\n')

print('Работающая дешифровка зная ключ')
print(decrypt(2, a), '\n')

print('Работающая дешифровка не зная ключ')
print(c, '\n')

print('Неработающая дешифровка не зная ключ потому что короткий текст')
print(d, '\n')

key = '1, 4, 9'
e = encrypt_(key, c)
f = decrypt_(key, e)

print('Работающая зашифровка Вернама')
print(e, '\n')

print('Расшифрованный текст шифра Вернама:')
print(f, '\n')
