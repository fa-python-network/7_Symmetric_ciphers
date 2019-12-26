def encript(s, key):
    t1 = [i for i in s]
    t2 = [key[i % len(key)] for i in range(len(t1))]
    t3 = [chr((ord(t1[i]) + ord(t2[i]))) for i in range(len(t1))]
    return ''.join(t3)


def decript(s, key):
    t1 = [i for i in s]
    t2 = [key[i % len(key)] for i in range(len(t1))]
    t3 = [chr((ord(t1[i]) - ord(t2[i]))) for i in range(len(t1))]
    return ''.join(t3)


word = 'absolutely breathtaking!'
key = 'password'
encript_word = encript(word, key)
decript_word = decript(encript_word, key)
print(encript_word)
print(decript_word)