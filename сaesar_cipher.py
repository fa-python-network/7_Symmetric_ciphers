#!/usr/bin/env python
# coding: utf-8

# In[87]:


def encrypt(k, m):
    lst = [chr((ord(i)+k)%65536) for i in m]
    return ''.join(lst)


def decrypt(k, c):
    lst = [chr((ord(i)-k)%65536) for i in c]
    return ''.join(lst)

code = encrypt(3, 'abcdefgh12345')
print("Encrypted message: " + code)

message = decrypt(3, code)
print("Decrypted message: " + message)

