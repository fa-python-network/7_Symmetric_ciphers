# 1114111 - max number for chr at the moment
def vigener_encipher(string, k):
    lb, rb = 0, 1114111
    res = ''
    for ind, s in enumerate(string):
        cur_k = ord(k[ind % len(k)])
        if ord(s) + cur_k > rb:
            res += chr(lb + cur_k - (rb - ord(s)) - 1)
        else:
            res += chr(ord(s) + cur_k)
    return res


def vigener_decipher(string, k):
    lb, rb = 0, 1114111
    res = ''
    for ind, s in enumerate(string):
        cur_k = ord(k[ind % len(k)])
        if ord(s) - cur_k < lb:
            res += chr(rb - cur_k + (ord(s) - lb) + 1)
        else:
            res += chr(ord(s) - cur_k)
    return res


s = 'qqqOne two three four five sex seven eight nine ten. And some other words to gain string size!'
new_s = vigener_encipher(s, 'qwe')
old_s = vigener_decipher(new_s, 'qwe')
print(f's = {s}\n'
      f'new_s = {new_s}\n'
      f'old_s = {old_s}')
