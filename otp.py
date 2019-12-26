def vernam (k, m):

    lb, rb = 0, 65536
    res = ''
    for ind, s in enumerate(m):
        cur_k = ord(k[ind % len(k)])
        res += chr(ord(s) ^ cur_k)
    return res



s = 'oh hi mark'
print("Исходная строка: " + s)
example1 = vernam('qwe', s)
print("\n Шифр:" + example1)
hack = vernam('qwe', example1)
print("\n Взлом шифра: " + hack)

