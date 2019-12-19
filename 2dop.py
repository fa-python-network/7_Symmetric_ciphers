import random, math
from functools import reduce


def generateOTP(count):
	string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	OTP = ""
	length = len(string)
	for i in range(count):
		OTP += string[math.floor(random.random() * length)]
	return OTP


def encode(string, key):
	iv = generateOTP(len(key))
	arr = [string[i:i + len(key)] for i in range(0, len(string), len(key))]
	if len(arr[-1]) < len(key):
		arr[-1] += " " * (len(key) - len(arr[-1]))
	arr = [[ord(j) for j in i] for i in arr]
	print(arr)
	arr[0] = [arr[0][i] ^ ord(iv[i]) ^ ord(key[i]) for i in range(len(key))]
	for i in range(1, len(arr)):
		arr[i] = [arr[i][t] ^ arr[i - 1][t] for t in range(len(key))]
	print(arr)
	arr.insert(0, [ord(j) for j in iv])
	return arr

def decode(line, key):
	arr = line
	result = []*(len(line)-1)
	for i in range(2, len(arr)):
		result.append([arr[i][t] ^ arr[i - 1][t] for t in range(len(key))])
	result.insert(0, [arr[1][i] ^ arr[0][i] ^ ord(key[i]) for i in range(len(key))])
	listMerge = lambda s: reduce(lambda d, el: d.extend(el) or d, s, [])
	return "".join(list(map(chr, listMerge(result))))

key = input()
string = input("Введите вашу строку:")
encodeString = encode(string, key)
decodeLine = decode(encodeString, key)
print(decodeLine)