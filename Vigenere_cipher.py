def incript(s, key):
    t1 = [i for i in s]
    t2 = [key[i % len(key)] for i in range(len(t1))]
    t3 = [chr((ord(t1[i]) + ord(t2[i]))) for i in range(len(t1))]
    return ''.join(t3)


def decript(s, key):
    t1 = [i for i in s]
    t2 = [key[i % len(key)] for i in range(len(t1))]
    t3 = [chr((ord(t1[i]) - ord(t2[i]))) for i in range(len(t1))]
    return ''.join(t3)


msg = 'Aspire to inspire before we expire'
key = 'password'
inc_msg = incript(msg, key)
dec_msg = decript(inc_msg, key)
print(inc_msg)
print(dec_msg)
