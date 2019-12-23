#
#
from random import randint

def encrypt(k, m):
    return ''.join([chr((ord(x) + k) % 65536) for x in m])

def decrypt(k, m):
    return ''.join([chr((ord(x) - k) % 65536) for x in m])

def nonkey(m):
    max_char = 0
    key = 0
    
    for i in range(65536):
        tt = len(m.split(chr((32 + i) % 65536)))
        
        if tt > max_char:
            max_char = tt
            key = i
            
    return key

def vernam(m):
    k = ''
    tt = ''
    fin = ''

    for i in m:
        k = randint(0,32)
        tt += str(k) + "/"
        fin += chr((ord(i) + k - 17)%33 + ord('А'))
    return [fin, tt]
        
#def dever(m, k):
#    k =  k.split('/')
#    m = ''
#    for i, s in enumerate(m):
#        if k[i] != '':
#            m += chr((ord(s) - int(k[i])- 17)%33 + ord('А'))
#    return m

a = vernam('Владимирский централ, ветер северный. Этапом из твери - зла немеренно. Лежит на средце тяжкий груз!')
print(a[0])
b = dever(a[0], a[1])
print(b)

#c = 6
#a = encrypt(c, 'Владимирский централ, ветер северный. Этапом из твери - зла немеренно. Лежит на средце тяжкий груз!')
#print(a)
#b = nonkey(a)
#print(decrypt(c, a))
#print(decrypt(b, a))