def decode_encode(text, key): #XOR
    ls = []
    for a in range(len(text)):
        for i, j in [(text[a], key[a])]:
            ls.append(ord(i) ^ ord(j))
    return "".join(map(chr, ls))


text = "Hello world"
key = "jgqwertagsh"
enc = decode_encode(text, key)

for i in enc:
    print(f"|{i}|")
dec = decode_encode(enc, key)
print(enc, dec)


