line = "Мама мыла раму№"
key = "354щшpоьусqtьz"


def encode(line, key):
	a, b = [i for i in (line, key)]
	result = "".join(map(chr, [ord(x) ^ ord(y) for x, y in [(a[i], b[i]) for i in range(len(a))]]))
	return result


def decode(line, key):
	a, b = [i for i in (line, key)]
	result = "".join(map(chr, [ord(x) ^ ord(y) for x, y in [(a[i], b[i]) for i in range(len(a))]]))
	return result


_encode = encode(line, key)
_decode = decode(_encode, key)
print(_decode, _encode, sep="\n")
