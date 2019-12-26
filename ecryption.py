msg = "A design is"
key = "354щшpоьусq"


def encrypt(msg, key):
	a, b = [i for i in (msg, key)]
	msg1 = "".join(map(chr, [ord(x) ^ ord(y) for x, y in [(a[i], b[i]) for i in range(len(a))]]))
	return msg1


def decrypt(msg1, key):
	a, b = [i for i in (msg1, key)]
	msg = "".join(map(chr, [ord(x) ^ ord(y) for x, y in [(a[i], b[i]) for i in range(len(a))]]))
	return msg


e = encrypt(msg, key)
d = decrypt(e, key)
print(e)
print(d)