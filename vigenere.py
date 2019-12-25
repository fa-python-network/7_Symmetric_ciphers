def incript(st, key):
    a1 = [i for i in st]
    a2 = [key[i % len(key)] for i in range(len(a1))]
    a3 = [chr((ord(a1[i]) + ord(a2[i]))) for i in range(len(a1))]
    return ''.join(a3)


def decript(st, key):
    a1 = [i for i in st]
    a2 = [key[i % len(key)] for i in range(len(a1))]
    a3 = [chr((ord(a1[i]) - ord(a2[i]))) for i in range(len(a1))]
    return ''.join(a3)


msg = 'hgfi hfdjddefg'
key = 'password'
new_msg = incript(msg, key)
new_new_msg = decript(new_msg, key)
print(new_msg)
print(new_new_msg)
