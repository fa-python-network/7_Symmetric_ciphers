import json
def encr(k,m):
    c = ""
    for i in m:
        c += chr(ord(i) + k)
    return c

def decr(k,c):
    m = ""
    for i in c:
        m += chr(ord(i) - k)
    return m

def hack(a):
    sl = {}
    for i in a:
        if i not in sl:
            sl[i] = 1
        else:
            sl[i] += 1
    sl = sorted(sl.items(), key = lambda x : x[1], reverse= True)
    sym = sl[0][0]
    print(sym)
    k = ord(sym) - ord(' ')
    return decr(k, a)

with open('a.json', 'r', encoding= 'UTF-8') as file:
    a = json.load(file)

a = encr(3, a)
#print(encr(3,'fire'))
print(hack(a))