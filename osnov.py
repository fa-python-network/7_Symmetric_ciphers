def caesar_encipher(k, m):
    lb, rb = 0, 65536
    res = ''
    for s in m:
        if ord(s) + k > rb:
            res += chr(lb + k - (rb - ord(s)) - 1)
        else:
            res += chr(ord(s) + k)
    return res


def caesar_decipher(k, c):
    lb, rb = 0, 65536
    res = ''
    for s in c:
        if ord(s) - k < lb:
            res += chr(rb - k + (ord(s) - lb) + 1)
        else:
            res += chr(ord(s) - k)
    return res

def vigener_encipher(k, m):
    lb, rb = 0, 1114111
    res = ''
    for ind, s in enumerate(m):
        cur_k = ord(k[ind % len(k)])
        if ord(s) + cur_k > rb:
            res += chr(lb + cur_k - (rb - ord(s)) - 1)
        else:
            res += chr(ord(s) + cur_k)
    return res


def vigener_decipher(k, c):
    lb, rb = 0, 65536
    res = ''
    for ind, s in enumerate(c):
        cur_k = ord(k[ind % len(k)])
        if ord(s) - cur_k < lb:
            res += chr(rb - cur_k + (ord(s) - lb) + 1)
        else:
            res += chr(ord(s) - cur_k)
    return res


s = 'oh hi mark'
k = 1
print("\n\nИсходная строка: \n" + s)
print("\n---\n")
example1 = caesar_encipher(k, s)
print("Шифр Цезаря:\n")
print("Шифр:" + example1)
hack = caesar_decipher(k, example1)
print("Взлом шифра: \n" + hack)
print("\n---\n")
print("Шифр Вижинера\n")
example2 = vigener_encipher('ключ', s)
print("Шифр: " + example2)
hack2 = vigener_decipher('ключ', example2)
print("Взлом: " + hack2)
print("\n---\n")

