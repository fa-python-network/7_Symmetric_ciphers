

def encrypt(k, msg):
    nmsg=''
    for ch in msg:
        ch = (ord(ch)+k) % 65536
        nmsg = nmsg + chr(ch)
    return nmsg

def decrypt(k, nmsg):
    msg=''
    for ch in nmsg:
        ch = (ord(ch) - k) % 65536
        msg = msg + chr(ch)
    return msg

def hack(nmsg):
    chars={}
    for ch in nmsg:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch]=1

    max_val = max(chars.values())
    final_dict = {k: v for k, v in chars.items() if v == max_val}
    key=get_key(final_dict,max_val)
    print(key)
    msg=decrypt((ord(key)-ord(' ')%65536),nmsg)

    return msg



def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def shifr_viginera_encrypt(key,msg):
    keys=''
    while len(keys)!=len(msg):
        for i in key:
            if len(keys)!=len(msg):
                keys=keys+i
            else:
                break
    nmsg=''
    for i in range(len(keys)):
        i=(ord(msg[i])-ord(keys[i]))%65536
        nmsg=nmsg+chr(i)
    return nmsg




def shifr_viginera_decrypt(key, msg):
    keys = ''
    while len(keys) != len(msg):
        for i in key:
            if len(keys) != len(msg):
                keys = keys + i
            else:
                break
    nmsg = ''
    for i in range(len(keys)):
        i = (ord(msg[i]) + ord(keys[i])) % 65536
        nmsg = nmsg + chr(i)
    return nmsg

def shifr_Varnera_XOR_encrypt(key,msg):
    nmsg=''
    for i in msg:
        i=ord(i) ^ ord(key)
        nmsg=nmsg + chr(i)
    return nmsg

def shifr_Varnera_XOR_decrypt(key,nmsg):
    msg = ''
    for i in nmsg:
        i = ord(i) ^ ord(key)
        msg = msg + chr(i)
    return msg




msg='Зеленский ответил на слова Путина по поводу газа'
print("Cezar")
print(msg)
nmsg=encrypt(16512, msg)
print(nmsg)
print(decrypt(16512, nmsg))
print(hack(nmsg)+"\n\n\n")

print("Viginer")
nmsg=shifr_viginera_encrypt('lop',msg)
print(nmsg)
print(shifr_viginera_decrypt('lop',nmsg)+"\n\n\n")

print("OTP")
nmsg=shifr_Varnera_XOR_encrypt('Ѯ',msg)
print(nmsg)
print(shifr_Varnera_XOR_decrypt('Ѯ',nmsg))