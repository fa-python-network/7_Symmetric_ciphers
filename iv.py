string = input('Введите текст: ')
key = 'ds2ag6'
iv = 'ripow2'

def enc(string, key, iv):
    chipher_string = ''
    for i in range(0, len(string), 5):
        new_string = ''
        for k, v in enumerate(string[i:i+5]):
            new_string += chr(ord(v) ^ ord(iv[k]))
        chipher = ''
        for k, v in enumerate(new_string):
            chipher += chr(ord(v) ^ ord(key[k]))
        chipher_string += chipher
        iv = chipher

    return chipher_string


def dec(chipher_string, key, iv):
    chipher_lst = []
    for i in range(0, len(chipher_string), 5):
        chipher_lst.append(chipher_string[i:i+5])
    chipher_lst.reverse()

    lst = []
    for k, v in enumerate(chipher_lst):
        str, str2 = '', ''
        for j, i in enumerate(v):
            str += chr(ord(i) ^ ord(key[j]))
        for j, i in enumerate(str):
            try:
                str2 += chr(ord(i) ^ ord(chipher_lst[k+1][j]))
            except IndexError:
                str2 += chr(ord(i) ^ ord(iv[j]))
        lst.append(str2)
    lst.reverse()

    return ''.join(lst)


chipher = enc(string, key, iv)
dechipher = dec(chipher, key, iv)

print(chipher)
print(dechipher)

