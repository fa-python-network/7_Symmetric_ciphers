#!/usr/bin/env python
# coding: utf-8

# In[120]:


a = 'Mr. and Mrs. Dursley of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much.'
def encrypt(k, m):
    lst = [chr((ord(i)+k)%65536) for i in m]
    return ''.join(lst)


def hack(c):
    dicti = {}
    for i in c:
        if ord(i) in dicti:
            dicti[ord(i)] +=1;
        else:
            dicti[ord(i)] = 1
    maximum = 0
    for k, v in dicti.items():
        if v > maximum:
            maximum = v
            key = k
    key = key - ord(' ')
    lst = [chr((ord(i)-key)%65536) for i in c]
    return ''.join(lst)


print("Encrypted message: " + encrypt(3, a))
print("\nHacked: " + hack(code))

