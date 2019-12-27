# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:41:54 2019

@author: 187056
"""
text='Wfggny%fsi%hfwwty%fwj%kwnjsix%&'

def encrypt(key,msg):
    stroka = ''
    for symbol in msg:
        num = ord(symbol)
        num += key
        stroka = stroka + chr(num)
    return stroka
def hack(stroka):
    vhod = []
    for i in range(len(stroka)):
        vhod.append([stroka.count(stroka[i]), stroka[i]])
        max = 0
        for j in range(len(vhod)):
            if vhod[j][0] > max:
                max = vhod[j][0]
                elmax = vhod[j][1]
    key = ord(elmax)-ord(' ')%256
    spisok_1 = []
    spisok_2 = []
    for i in stroka:
        spisok_1.append((ord(i)-key)%256)
    for i in range(len(spisok_1)):
        spisok_2.append(chr(spisok_1[i]))
    result = ''.join(spisok_2)
    return result



print('Ваше предложение: ', text)               
rt = hack(text) 
print('Расшифрованое предложение:  ', rt)       

