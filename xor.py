
def rer(string, key):
	words = []
	while len(string) >= len(key):
		words.append(string[:len(key)])
		string = string[len(key):]
	if len(string) != 0:
		words.append(string)
	return ''.join([''.join([chr(ord(word[i]) ^ ord(key[i])) for i in range(len(list(word)))]) for word in words])


def out_rer(string, key):
	words = []
	while len(string) >= len(key):
		words.append(string[:len(key)])
		string = string[len(key):]
	if len(string) != 0:
		words.append(string)
	return ''.join([''.join([chr(ord(word[i]) ^ ord(key[i])) for i in range(len(list(word)))]) for word in words])


string = 'ArtysH'
key = '123'
word = rer(string, key)
print(word)
print(out_rer(word, key))


