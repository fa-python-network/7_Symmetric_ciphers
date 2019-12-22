def block_chain_encipher(string, k, iv=None, start=0):
    from random import randint

    if len(string) % len(k):
        space_count = len(k) - len(string) % len(k)
        string += ' ' * space_count
        print(f'Строка была дополнена {space_count} пробелами')

    lb, rb = 0, 1114111
    if iv is None:
        iv = ''.join([chr(randint(lb, rb)) for _ in range(len(k))])

    res = ''
    for ind, s in enumerate(string[start:start + len(k)]):
        cur_code = ord(s) ^ ord(iv[ind]) ^ ord(k[ind])
        assert cur_code <= rb, f'Can not encipher symbol "{s}", try encryption again'

        res += chr(cur_code)

    if start + len(k) < len(string):
        if start == 0:
            return res + block_chain_encipher(string, k, iv=res, start=start + len(k)), iv
        else:
            return res + block_chain_encipher(string, k, iv=res, start=start + len(k))

    return res


def block_chain_decipher(string, k, iv, end=None):
    lb, rb = 0, 1114111
    
    if end is None:
        end = len(string)

    start = end - len(k)
    res = ''
    for ind, s in enumerate(string[start:end]):
        cur_code = ord(s) ^ ord(iv[ind] if start == 0 else string[start - len(k) + ind]) ^ ord(k[ind])
        assert cur_code <= rb, f'Can not decipher symbol "{s}"'

        res += chr(cur_code)

    if end == len(string):
        res = res.strip()  # убираем возможные дополнительные пробелы в конце последнего блока

    if start != 0:
        return block_chain_decipher(string, k, iv, end=start) + res

    return res



s = 'qqqOne two three four five sex seven eight nine ten. And some other words to gain string size!'
new_s, iv = block_chain_encipher(s, 'qwe')
old_s = block_chain_decipher(new_s, 'qwe', iv)
print(f's = {s}\n'
      f'new_s = {new_s}\n'
      f'old_s = {old_s}')
