import random

def cezar_encrypt(k, m):
    out_str = ''
    for i in m:
        out_str += chr((ord(i) + k) % 65536)
    return out_str

def cezar_decrypt(k, m):
    out_str = ''
    for i in m:
        out_str += chr((ord(i) - k) % 65536)
    return out_str

def cezar_hac(m):
    max_char_ = 0
    key = 0
    for i in range(65536):
        prob = len(m.split(chr((32 + i) % 65536)))
        if prob > max_char_:
            max_char_ = prob
            key = i
    return key


def Vijiner_encrypt(text, key, IV = random.getrandbits(10)):
    casha = ''
    pred = 0
    for ind, i in enumerate(text):
        if casha == '':
            pred = IV ^ ord(key[0]) ^ ord(text[0])
            print(pred)
            casha = chr(pred)
        simv = pred ^ ord(key[ind % len(key)]) ^ ord(i)
        pred = simv
        casha += chr(simv)
    casha = str(IV) +"-IV-" + casha
    return casha


fff = cezar_encrypt(547, "aasda asdaa aasd affg a ghhaa a jaj j jjkj j jj sfr hrt wrh rtw her t")
print(fff)

key = cezar_hac(fff)
print(key)

fff = cezar_decrypt(key, fff)
print(fff)

print('-------------------')

first = Vijiner_encrypt('asdsdfghjkldxcfvghbjnkm', 'aasdasdasd')
print(first)
