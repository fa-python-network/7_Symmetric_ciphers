import random


def encrypt(msg, key):
    IV = chr(random.getrandbits(8))
    print('IV: ', IV)
    enc_msg = ''
    for ind, char in enumerate(msg):
        if enc_msg == '':
            prev = chr(ord(char) ^ ord(IV) ^ ord(key[ind % len(key)]) )
            enc_msg += prev
        else:
            prev = chr(ord(char) ^ ord(prev) ^ ord(key[ind % len(key)]))
            enc_msg += prev
    enc_msg = IV + enc_msg
    return enc_msg


def decrypt(secret, key):
    IV = secret[0:1]
    print('IV: ', IV)
    enc_msg = secret[1:]
    dec_msg = ''
    for ind, char in enumerate(enc_msg):
        if dec_msg == '':
            prev = chr(ord(char) ^ ord(key[ind % len(key)]) ^ ord(IV))
            dec_msg += prev
        else:
            prev = chr(ord(char)  ^ ord(enc_msg[ind-1]) ^ ord(key[ind % len(key)]))
            dec_msg += prev
    return dec_msg


mess = encrypt('bird', 's')
print('encrypt: ', mess)
ssem = decrypt(mess, 's')
print('decrypt: ', ssem)
