def feistel_encipher(string):
    def pair_encipher(l, r):
        F = lambda l, i: (l + i) % 1114111

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
        F = lambda l, i: (l + i) % 1114111

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


s = 'qqqOne two three four five sex seven eight nine ten. And some other words to gain string size!!'
new_s = feistel_encipher(s)
old_s = feistel_decipher(new_s)
print(f's = {s}\n'
      f'new_s = {new_s}\n'
      f'old_s = {old_s}')
