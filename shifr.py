import json

def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d

def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict() 

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code

def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic 

def full_encode(value, key):
    dic = comparator(value, key)
    #print('Compare full encode', dic)
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis

def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict() 

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code


def full_decode(value, key):
    dic = comparator(value, key)
    d = form_dict() 
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis


if __name__ == "__main__":
    with open('a.json', 'r', encoding= 'UTF-8') as file:
        word = json.load(file)

    #word = 'Welcome to the club buddy'
    key = 'holiday'
    
    print(word)
    #print(key)

    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
 
    #print('Value= ',value_encoded)
    #print('Key= ', key_encoded)

    shifre = full_encode(value_encoded, key_encoded)
    print('---------------------------------------------------------------------------------------------------')
    print('Shifre: ', ''.join(decode_val(shifre)))

    decoded = full_decode(shifre, key_encoded)
    decode_word_list = decode_val(decoded)
    print('---------------------------------------------------------------------------------------------------')
    print('File: ',''.join(decode_word_list))