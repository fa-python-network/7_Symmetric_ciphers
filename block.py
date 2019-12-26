
def rer(string, key):
	words = []
	while len(string) >= len(key):
		words.append(string[:len(key)])
		string = string[len(key):]
	if len(string) != 0:
		words.append(string)
	return words


def block(string, iv, key):
	sh = []
	words = rer(string, iv)
	words[0] = ''.join([chr(ord(words[0][i]) ^ ord(iv[i]))  for i in range(len(words[0]))])
	sh.append(words[0])
	while len(words) > 1:
		iv_ = words[0]
		words[1] = ''.join([chr(ord(words[1][i]) ^ ord(iv_[i]) ^ ord(key[i]))  for i in range(len(words[1]))])
		sh.append(words[1])
		words = words[1:]
	return ''.join(sh)


def block_out(word, iv, key):
	words = rer(word, key)
	sh = []
	sh.append( ''.join([chr(ord(words[0][i]) ^ ord(iv[i]))  for i in range(len(words[0]))]))
	while len(words) > 1:
		iv_ = words[-2]
		words[-1] = ''.join([chr(ord(words[-1][i]) ^ ord(iv_[i]) ^ ord(key[i])) for i in range(len(words[-1]))])
		sh.append(words[-1])
		words = words[:-1]
	return ''.join(sh)


string = 'Artysh'
key = '123'
iv = 'abc'

word = block(string, iv, key)

print(block_out(word, iv, key))

