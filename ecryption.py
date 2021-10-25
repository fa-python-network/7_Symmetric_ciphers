import random

STRING = "A Londoner was going to the west of England for a holiday. \
He arrived at a small town by train. When he knew that there were two hotels there, \
he took a taxi. On the way out of the station he asked the driver: «How long have \
you been living here?» «Since childhood,» — was the answer. «Then which hotel could \
you recommend?» asked the tourist. «You see, it makes no difference — whichever hotel \
you’ll choose you’ll be sorry you didn’t choose the other,» answered the driver."
MUL = 200

def encrypt(k, m):
    return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))

encrypted = encrypt(2, STRING)
print("-"*MUL)
print(encrypted)
print("-"*MUL)
decrypted = decrypt(2, encrypted)
print(decrypted)
print("-"*MUL)

def auto_decrypter(text):
    container = []
    for el in set(text):
        container.append((el, text.count(el)))
    container.sort(key = lambda x:x[1] , reverse = True)
    shifts = [ord(" ") - ord(el[0]) for el in container]
    for shift in shifts:
        decrypted = encrypt(shift, text)
        print(decrypted)
        cmd = input("Если текст читаем - введите любой символ, иначе Enter!   ")
        if cmd:
            return shift
        
    return None

print("Свдиг: ", - auto_decrypter(encrypted))
print("-"*MUL)

def encrypt_Vernam(text, key = None):
    text_len = len(text)
    if not key:
        key = ''.join([chr(random.randint(0,65535)) for _ in range(text_len)])
    encrypted_text = ''.join([chr(ord(text[i])^ord(key[i])) for i in range(text_len)])
    return encrypted_text, key

encrypted, key = encrypt_Vernam(STRING)
decrypted, key = encrypt_Vernam(encrypted, key)
print(decrypted)
print("-"*MUL)

def encode_CPC(text, key = None, vector = None):
    if key:
        block_size = len(key)
    else:
        block_size= 32
        key = ''.join([chr(random.randint(0,65535)) for _ in range(block_size)])
    if not vector or (len(vector) != block_size):
        vector = ''.join([chr(random.randint(0,65535)) for _ in range(block_size)])
    return cipher_block_chaining(text, key, vector), key, vector


def cipher_block_chaining(text, key, vector):
    if not text:
        return ""
    block_size = len(key)
    summary_text = encrypt_Vernam(text[:block_size], vector)[0]
    encrypted = encrypt_Vernam(summary_text, key)[0]
    return encrypted + cipher_block_chaining(text[block_size:], key, encrypted)

def decode_CPC(encrypted, key, vector):
    if not encrypted:
        return ""
    block_size = len(key)
    block = len(encrypted) % block_size
    block = block_size if not block else block
    summary_text = encrypt_Vernam(encrypted[-block:], key)[0]
    previous_vector = vector if len(encrypted) <= block_size else encrypted[- block - block_size: - block]
    decrypted = encrypt_Vernam(summary_text, previous_vector)[0]
    return decode_CPC(encrypted[:-block], key, vector) + decrypted


encrypted, key, vector = encode_CPC(STRING)
decrypted = decode_CPC(encrypted, key, vector)
print(decrypted)
print("-"*MUL)
