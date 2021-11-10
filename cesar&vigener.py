def coding (st, key): #кодирование Цезарь
    s = list(st)
    for i in range(len(s)):
        j = ord(s[i])
        j += key
        j = chr(j)
        s[i] = j

    return(''.join(s))
    
def decoding (st, key): #декодирование Цезарь
    s = list(st)
    for i in range(len(s)):
        j = ord(s[i])
        j -= key
        j = chr(j)
        s[i] = j
    return(''.join(s))
    
def find_key (st): #поиск ключа Цезарь
    s = list(st)
    d = {}
    for i in range(len(s)):
        try:
            d[s[i]] += 1
        except:
            d[s[i]] = 1
    print (d)
    mx = 0
    for k in d.keys():
        if d[k] > mx:
            mx = d[k]
            let = k
    print(mx)
    print(let)
    key = ord(let) - ord(" ")
    print(key)
    s = decoding(st, key)
    return s

def coding_v(st, key): #кодирование Виженером
    s = list(st)
    k = list(key)
    for i in range(len(k)):
        k[i] = ord(k[i])
    print(k)
    g = 0
    for i in range(len(s)):
        true_key = k[g % len(k)]
        j = ord(s[i]) 
        j += true_key
        j = chr(j % 255)
        s[i] = j
        g += 1
    st = ''
    for i in s:
        st += i
    return st
    
def decoding_v(st, key): #декодирование Виженер
    s = list(st)
    k = list(key)
    for i in range(len(k)):
        k[i] = ord(k[i])
    print(k)
    g = 0
    for i in range(len(s)):
        true_key = k[g % len(k)]
        j = ord(s[i]) 
        j -= true_key
        j = chr(j % 255)
        s[i] = j
        g += 1
    st = ''
    for i in s:
        st += i
    return st
#основная часть примера работы функций
msg = "Unix is a family of portable, multitasking and multi-user operating systems that are based on the ideas of the original AT&T Unix project."
new = coding(msg,3)
print(find_key(new))
msg = "Unix is a family of portable, multitasking and multi-user operating systems that are based on the ideas of the original AT&T Unix project."
key = "key"
print(msg)
new = coding_v(msg, key)
print(new)
print(decoding_v(new,key))
