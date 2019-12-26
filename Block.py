def block_chain_encipher(k, c, iv=None, start=0):
    from random import randint

    if len(c) % len(k):
        space_count = len(k) - len(c) % len(k)
        c += ' ' * space_count
        print(f'Строка была дополнена {space_count} пробелами')

    lb, rb = 0, 65536
    if iv is None:
        iv = ''.join([chr(randint(lb, rb)) for _ in range(len(k))])

    res = ''
    for ind, s in enumerate(c[start:start + len(k)]):
        cur_code = ord(s) ^ ord(iv[ind]) ^ ord(k[ind])
        assert cur_code <= rb, f'Can not encipher symbol "{s}", try encryption again'

        res += chr(cur_code)

    if start + len(k) < len(c):
        if start == 0:
            return res + block_chain_encipher(k, c, iv=res, start=start + len(k)), iv
        else:
            return res + block_chain_encipher(k, c, iv=res, start=start + len(k))

    return res


def block_chain_decipher(k, c, iv, end=None):
    lb, rb = 0, 65536
    
    if end is None:
        end = len(c)

    start = end - len(k)
    res = ''
    for ind, s in enumerate(c[start:end]):
        cur_code = ord(s) ^ ord(iv[ind] if start == 0 else c[start - len(k) + ind]) ^ ord(k[ind])
        assert cur_code <= rb, f'Can not decipher symbol "{s}"'

        res += chr(cur_code)

    if end == len(c):
        res = res.strip()  # убираем возможные дополнительные пробелы в конце последнего блока

    if start != 0:
        return block_chain_decipher(k, c, iv, end=start) + res

    return res



s = 'oh hi mark'
print("Исходная строка: " + s)
example1, iv = block_chain_encipher('ключ', s)
print("\nШифр:" + example1)
hack = block_chain_decipher('ключ', example1, iv)
print("\nВзлом шифра: " + hack)
print("\n")
