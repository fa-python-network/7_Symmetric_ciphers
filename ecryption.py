def Encrypt_XOR(key,iv,m):
    string = ''
    reset_iv = ''
    for i in range (len(m)):
        string += chr(ord(m[i]) ^ ord(key[i % len(k)]) ^ ord(iv[i % len(iv)]))
        reset_iv += chr(ord(m[i]) ^ ord(key[i % len(k)]) ^ ord(iv[i % len(iv)]))
        if len(reset_iv) == len(key):
            iv = reset_iv
            reset_iv = ''
    return string
def Decrypt_XOR(key,iv,m):
    string = ''
    reset_iv = ''
    for i in range (len(m)):
        reset_iv += m[i]
        string += chr(ord(m[i]) ^ ord(key[i % len(k)]) ^ ord(iv[i % len(iv)]))
        if len(reset_iv) == len(key):
            iv = reset_iv
            reset_iv = ''
    return string
m = 'Affdfsfw'
k = 'KEY'
i = 'OMG'
l = Encrypt_XOR(k,i,m)
print(l)
print(Decrypt_XOR(k,i,l))
