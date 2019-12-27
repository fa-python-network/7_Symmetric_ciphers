#!/usr/bin/env python
# coding: utf-8

# In[62]:


def encrypt(k, m):
    lst_m = [ord(i) for i in m]
    lst_k = [ord(k[i % len(k)]) for i in range(len(lst_m))]
    lst_cr = [chr((e + lst_k[i])%65536) for i, e in enumerate(lst_m)]
    return ''.join(lst_cr)
 
code = encrypt('harry', 'abcdefgh12345')
print(code)

def decrypt(k, c):
    lst_c = [ord(i) for i in c]
    lst_k = [ord(k[i % len(k)]) for i in range(len(lst_c))]
    lst_cr = [chr((e - lst_k[i])%65536) for i, e in enumerate(lst_c)]
    return ''.join(lst_cr)

print(decrypt('harry', code))

