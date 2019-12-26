def encrypt_caesar(text,key):
'Шифр Цезаря'
main_text = list(text)
end_text = []
for x in main_text:
x = ord(x)
x += int(key)
if x>= 65536:
x -= 65536
x = chr(x)
end_text.append(x)
return ''.join(end_text)

def encript_Vernam(text, key):
'Шифр Вернама'
main_text = list(text)
main_key = list(key)
counter = 0
end_text = []
for x in main_text:
if main_key == '':
main_key = list(input('Ключ не введен. Введите ключ: '))
else_key = main_key[(counter%len(main_key))]
x = ord(x)
x += ord(else_key)
x = chr(x)
counter += 1
end_text.append(x)
return ''.join(end_text)

print(encrypt_caesar("готово!", 3))
print(encript_Vernam("Готоово!!", "2"))
