# 1) Написать функцию шифрования и дешифрования текста обобщенным шифром Цезаря.

#import modules
from typing import Counter

print('\nРезультаты работы функций\n')

#Examle of data to encrypt
string = 'h e ll o world'

#Enter your key here
key = 2

#encryption function
def encrypt(key, data):

    max = 65536
    min = 0

    #create list of coded letters
    list_of_numbers = []
    for letter in data:
        code_letter = ord(letter)
        list_of_numbers.append(code_letter)

    #add key to each number
    for number in range(len(list_of_numbers)):
        #check for max number
        if (list_of_numbers[number] + key) > max:
            number_add = min #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            number_add = key - (max-list_of_numbers[number])
            list_of_numbers[number] = min
            list_of_numbers[number] += number_add
        else:
            list_of_numbers[number] = list_of_numbers[number] + key 

    #transform list of numbers back into string
    result = ''
    for number in list_of_numbers:
        result = result + str(chr(number))
    
    return result

#Decryption function
def decrypt(key, data):
    
    max = 65536
    min = 0

    #create list of coded letters
    list_of_numbers_to_decode = []
    for letter in data:
        code_letter = ord(letter)
        list_of_numbers_to_decode.append(code_letter)
    
    #subtract key from each number
    for number in range(len(list_of_numbers_to_decode)):
        #check for min number
        if (list_of_numbers_to_decode[number] - key) < min:
            number_substract = key - list_of_numbers_to_decode[number]
            list_of_numbers_to_decode[number] = max - number_substract
        else:
            list_of_numbers_to_decode[number] = list_of_numbers_to_decode[number] - key

    #transform list of numbers back into string
    result = ''
    for number in list_of_numbers_to_decode:
        result = result + str(chr(number))
    
    return result

#Examle of data to decrypt (In this case it is a data for back encrypted text to normal)
string2 = encrypt(key,string)

print('1 задание (Написать функцию шифрования и дешифрования текста обобщенным шифром Цезаря.)')
print('Initial text: ', string)
print('Encrypted text: ', encrypt(key,string))
print('Decrypted text: ', decrypt(key,string2))





# 2) Написать функцию, принимающую шифротекст, зашифрованный шифром из предыдущего задания и восстанавливающий текст, без знания ключа.

string_to_hack = encrypt(key,string)


#Function to hack encrypted text
def Hack(data):
    #find the most common element
    counter = {}
    for i in data: 
        counter[i] = counter.get(i, 0) + 1
    most_common_element = sorted([ (freq,word) for word, freq in counter.items() ], reverse=True)[:1][0][1]
    number_of_the_most_common_element = ord(most_common_element)
    
    #number of space
    space = 32
    
    #calculate key
    key = number_of_the_most_common_element - space

    return key

print('\n2 задание (Написать функцию, принимающую шифротекст, зашифрованный шифром из предыдущего задания и восстанавливающий текст, без знания ключа.)')
print('Encrypted text: ', string_to_hack)
print('Decrypted text: ', decrypt(Hack(string_to_hack), string_to_hack) ) #Hack(string_to_hack) - key; string_to_hack - encrypted text




#3)Реализовать в виде функций шифр Вернама.

#Function to encrypt text
def Ver1_enc(key, data):
    key = key * (len(data) // len(key)) + key[:(len(data) % len(key))]
    return ''.join(map(chr, [i ^ x for i, x in zip(map(ord, data), map(ord, key))]))

#Function to decrypt texxt
def Ver2_dec(key, data):
    return Ver1_enc(key, data)

#Vernam key
ver_key = "1 2 6 4 3"

#initial Vernam text
ver_data = 'hello '

#encrypted  Vernam text
ver_data_enc = Ver1_enc(ver_key,ver_data)

print('\n3 задание (Реализовать в виде функций шифр Вернама.)')
print('inintial Vernam text: ', ver_data)
print('encrypted Vernam text: ', Ver1_enc(ver_key,ver_data))
print('decrypted Vernam text: ', Ver2_dec(ver_key, ver_data_enc))