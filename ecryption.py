# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:58:00 2019

@author: polin
"""
import random

def xor(text,key):
    """ XOR двух текстов (одинаковой длины) """
    result=str()
    for i in range(len(key)):
        text_ord=ord(text[i]) 
        key_ord=ord(key[i])
        result+=chr(text_ord^key_ord)
    return result
       

def segment(message, key_length,num=None):
    """ Сегментирование текста по размеру ключа. 
    Возвращает список сегментов либо сегмент под определённым номером """
    if not num:
        num_of_segments=int(len(message)/key_length)
        result=[message[i*key_length:(i+1)*key_length]for i in range(num_of_segments)]
    else:
        result=message[num*key_length:(num+1)*key_length]
    return result

def add_char(message,key_length,char=" "):
    """ Дополнение сообщение символами для кратности длине ключа """
    if (len(message)%key_length!=0):
        message+=char*(key_length-(len(message)%key_length))
    return message

def randomize(length):
    """ Генерация строки случайных символов """
    result=str()
    for i in range(length):
        result+=chr(random.randint(0,2048))
    return result

def encrypt(message,key,iv):
    """ Шифрование текста """
    result=list()
    message=add_char(message,len(key)) # добиваем сообщение и IV до кратности
    iv=add_char(iv,len(key))           # длине ключа
    segmented_message=segment(message,len(key)) # сегментируем сообщение
    num_of_segments=len(segmented_message)
    
    result.append(iv) # добавляем IV в шифроткст
    result.append(xor(segmented_message[0],iv)) 
    
    for i in range(num_of_segments-1): 
        encrypted_segment=xor(result[i+1],segmented_message[i+1])
        encrypted_segment=xor(encrypted_segment,key)
        result.append(encrypted_segment)
    
    return "".join(result)

def decrypt(message,key):
    result=list()
    segmented_message=segment(message,len(key))
    iv=segmented_message[0]
    num_of_segments=len(segmented_message)   
    
    for i in range(num_of_segments):
        decrypted_segment=xor(xor(segmented_message[-i],key),segmented_message[-i-1])
        result.append(decrypted_segment)
    
    result=result[::-1]
    return "".join(result)

message="На практике в шифрах, наподобие Вижинера используется функция XOR вместо сложения. Она обладает большей равномерностью, не требует взятия модуля и обратна самой себе."
key=randomize(4)
iv=randomize(4)

print("Сообщение {}".format(message))
print("Ключ {}".format(key))
print("IV {}".format(iv))

encrypted=encrypt(message,key,iv)
print("Зашифрованное сообщение {}".format(encrypted))


decrypted=decrypt(encrypted,key)
print("Дешифрованное сообщение {}".format(decrypted))
