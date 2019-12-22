def vigener_vernam_cipher(string, k):
    """Шифр Вижинера + шифр Вернама"""

    lb, rb = 0, 1114111
    res = ''
    for ind, s in enumerate(string):
        cur_k = ord(k[ind % len(k)])
        res += chr(ord(s) ^ cur_k)
    return res



s = 'qqqOne two three four five sex seven eight nine ten. And some other words to gain string size!'
new_s = vigener_vernam_cipher(s, 'qwe')
old_s = vigener_vernam_cipher(new_s, 'qwe')
print(f's = {s}\n'
      f'new_s = {new_s}\n'
      f'old_s = {old_s}')
