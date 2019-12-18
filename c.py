
IV = ord('ڧ')


def e(k: str, p: str) -> str:
    c = ''
    xor_key = IV

    for i, s in enumerate(p):
        xor_key = ord(s) ^ xor_key ^ ord(k[i % len(k)])
        c += chr(xor_key)
    
    return c


def d(k: str, c: str) -> str:
    p = ''
    xor_key = IV

    for i, s in enumerate(c):
        p += chr(ord(s) ^ ord(k[i % len(k)]) ^ xor_key)
        xor_key = ord(s)
    
    return p


k = 'πbluh'
p = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.'
print(p)

print('---------------------')

# encrypt
c = e(k, p)
print(c)

print('---------------------')

# decrypt
p = d(k, c)
print(p)
