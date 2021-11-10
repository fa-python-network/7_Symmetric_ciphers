def xor(st, key):
    encript_str = ""
    key = str(key)
    t = 0
    for i in st:
        encript_str += chr(ord(i) ^ ord(key[t % len(key)]))
        t += 1 
    return  encript_str   

strg = "unix or smth new"
key  = "help"
print("original: ",strg)
encr_strg = xor(strg, key) 
print("encript: ", encr_strg)
print("decript: ", xor(encr_strg, key))
