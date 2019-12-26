import json

def  code(k,m):
    c = ""
    for i in m:
        c+= chr(ord(i) + k)
    return c

def decode(k,c):
    m = ""
    for i in c:
        m+= chr(ord(i) - k)
    return m

def hack(a):
    s1 = {}
    for i in a:
        if i not in s1:
            s1[i] = 1
        else:
            s1[i]+=1
    s1 = sorted(s1.items(), key = lambda x: x[1], reverse = True) 
    sym = s1[0][0]
    print(sym)
    k = ord(sym) - ord(' ')
    return decode(k,a)

a = "Its no news that the future of communication is visual."

print(code(3,a))
print(hack(code(3,a)))

