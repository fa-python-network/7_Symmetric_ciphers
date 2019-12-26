# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:04:00 2019

@author: vlad
"""
def decript_caesar(text):
'Расшифровывает шифр Цезаря'

main_text = list(text)
end_text = []
mb_symbol = max(set(main_text), key=main_text.count)
expect_key = ord(mb_symbol) - ord(' ')
for x in main_text:
x = ord(x)
x -= int(expect_key)
if x < 0:
x += 65336
x = chr(x)
end_text.append(x)
end_text = ''.join(end_text)
return end_text

print(decript_caesar("в#Еогз#л#шсъц#тлфгхя$"))
