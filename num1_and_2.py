# 1114111 - max number for chr at the moment
def caesar_encipher(string, k):
    lb, rb = 0, 1114111
    res = ''
    for s in string:
        if ord(s) + k > rb:
            res += chr(lb + k - (rb - ord(s)) - 1)
        else:
            res += chr(ord(s) + k)
    return res


def caesar_decipher(string, k):
    lb, rb = 0, 1114111
    res = ''
    for s in string:
        if ord(s) - k < lb:
            res += chr(rb - k + (ord(s) - lb) + 1)
        else:
            res += chr(ord(s) - k)
    return res


def caesar_no_key_decipher(string):
    from collections import Counter

    awl = 5  # average words length
    if len(string) < awl * 10:
        print('Строка скорее всего содержит меньше 10 слов, так что высока вероятность ошибочной расшифровки')

    d = Counter(string)
    deciphered_space = d.most_common()[0][0]  # 'qweqweq' -> [('q', 3), ('w', 2), ('e', 2)]
    k = ord(deciphered_space) - ord(' ')

    lb, rb = 0, 1114111
    res = ''
    for s in string:
        if ord(s) - k < lb:
            res += chr(rb - k + (ord(s) - lb) + 1)
        else:
            res += chr(ord(s) - k)
    return res


s = 'One two three four five sex seven eight nine ten. And some other words to gain string size!'
k = 1
new_s = caesar_encipher(s, k)
old_s = caesar_decipher(new_s, k)
old_s_with_no_key = caesar_no_key_decipher(new_s)
print(f's = {s}\n'
      f'new_s = {new_s}\n'
      f'old_s = {old_s}\n'
      f'old_s_with_no_key = {old_s_with_no_key}')
