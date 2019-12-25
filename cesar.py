word = input('Введите текст \n')
a=''.join([chr(ord(i) + 3) for i in word])
print(a)



print(''.join([chr(ord(i) - 3) for i in a]))