# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:31:00 2019

@author: 181416
"""

def encode(stroka, key):
    list_str, list_key = [i for i in (stroka, key)] #2 списка a и b элементов строки и ключа
    ls=[]
    for a in range(len(list_str)): #идеим по длине строки
        for i, j in [(list_str[a],list_key[a])]: #идем по элементам двух списков символов строки и ключа
            ls.append(ord(i) ^ ord(j)) #побитовое или(XOR)
    rez= "".join(map(chr,ls)) # соединяем в строку все эелементы после побитового или
    return rez

def decode(stroka, key):
    list_str, list_key = [i for i in (stroka, key)]
    ls=[]
    for a in range(len(list_str)):
        for i , j in [(list_str[a],list_key[a])]:
            ls.append(ord(i) ^ ord(j))
    rez= "".join(map(chr,ls))
    return rez

stroka = "Простая строка текста"
key =    "142srtyuinmkjerplxdft"
enc = encode(stroka, key) #закодированное предложение
dec = decode(enc, key) #раскодированное предложение
print(enc, dec)