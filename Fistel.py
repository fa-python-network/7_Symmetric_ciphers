def feistel_encipher(string):
    def pair_encipher(l, r):
        F = lambda l, i: (l + i) % 65536

        if type(l) == str:
            l = ord(l)
        if type(r) == str:
            r = ord(r)

        for i in range(3):
            nxt = r ^ F(l, i)
            if i == 2:
                r = nxt
            else:
                l, r = nxt, l

        return chr(l) + chr(r)

    if len(string) % 2 != 0:
        string += ' '
        print('При шифровании был добавлен пробел')

    res = ''
    for i in range(0, len(string), 2):
        res += pair_encipher(string[i], string[i + 1])

    return res


def feistel_decipher(string):
    def pair_decipher(l, r):
        F = lambda l, i: (l + i) % 65536

        if type(l) == str:
            l = ord(l)
        if type(r) == str:
            r = ord(r)

        for i in range(2, -1, -1):
            nxt = r ^ F(l, i)
            if i == 0:
                r = nxt
            else:
                l, r = nxt, l

        return chr(l) + chr(r)

    res = ''
    for i in range(0, len(string), 2):
        res += pair_decipher(string[i], string[i + 1])

    return res.strip()


s = 'oh hi mark'
print("Исходная строка: " + s)
example1 = feistel_encipher(s)
print("\nШифр:" + example1)
hack = feistel_decipher(example1)
print("\nВзлом шифра: " + hack)
