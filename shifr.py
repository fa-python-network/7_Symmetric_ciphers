# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 08:42:31 2019

@author: 187056
"""

msg = "кролик" #передвав. сообщение
key = 5
def encrypt(key,msg):
    stroka = ''
    for symbol in msg:
        num = ord(symbol)
        num += key
        stroka = stroka + chr(num)
    return stroka
def decrypt(key, stroka_2):
    stroka_3 = ''
    for symbol in stroka_2:
        num = ord(symbol)
        num = (num - key)%65536
        stroka_3 = stroka_3 + chr(num)
    return stroka_3






  
print("Исходное сообщение: " + msg )    
print("Зашифрованное сообщение: ")    
nmsg = encrypt(key, msg)
print(nmsg)
print("Расшифрованное сообщение: ")
print(decrypt(key, nmsg))

        