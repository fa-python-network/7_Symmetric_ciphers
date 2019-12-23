#
#
from random import randint
from re import findall


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

def regular(text):
    template = r"[0-9]+"
    return findall(template, text)

def vernam(m, tt = '', k = ''):
    for i in m:
            key = randint(0,32); k += str(key) + "/"
            tt += chr((ord(i) + key - 17)%33 + ord('А'))
    return [tt, k]
    
def dever(m, k, tt = ''):
        for index, i in enumerate(m):
            tt += chr((ord(i) - int(regular(k)[index]) - 17)%33 + ord('А'))
        return tt

#x = 6
#a = encrypt(x, 'Натуральный блондин! На всю страну такой один!')
#print(a)
#c = nonkey(a)
#print(decrypt(x, a))
#print(decrypt(c, a))


#a = vernam('Листья с клена падают, с ясеня. Ничего себе, ничего себе! Вот смотрю я и действительно. Хорошо, хорошо!')
#print(a[0])
#b = dever(a[0], a[1])
#print(b)