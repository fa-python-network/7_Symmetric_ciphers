import random 
m = "Hello! Ya sdelal osnovnie zadania"
print(m)

def encrypt(k, m):
    iv = chr(random.getrandbits(10))
    spic_zakod = []
    spic_zakod.append(iv)
    for i in range(0, len(m)):
        if i == 0:
            simv = chr(ord(m[i])^ord(iv)^ord(k))
        else:
            simv = chr(ord(m[i])^ord(spic_zakod[i-1])^ord(k))
        spic_zakod.append(simv)
    stroka = ""
    for i in range(0,len(spic_zakod)):
        stroka = stroka + stroka.join(spic_zakod[i])
    return stroka

x = encrypt("w", m)
print(x)

def decrypt(k, c):
    spic_zakod = []
    iv = c[0]
    for i in range(1, len(c)):
        if i == 1:
            simv = chr(ord(c[i])^ord(iv)^ord(k))
        else:
            simv = chr(ord(c[i])^ord(k)^ord(c[i-2]))
        spic_zakod.append(simv)
    stroka = ""
    for i in range(0,len(spic_zakod)):
        stroka = stroka + stroka.join(spic_zakod[i])
    return stroka

y = decrypt("w", x)
print(y)