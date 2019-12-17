'''
Тут будет тело программы
'''

class Enigma():

    def encrypt_by_number(self,text,key):
        '''
        Зашифровывает текст методом Цезаря
        '''
        text = list(text)
        new_text = []
        for i in text:
            i=ord(i)
            i+= int(key)
            i=chr(i)
            new_text.append(i)
        new_text = ''.join(new_text)
        return new_text

    def encript_by_key_name(self, text, key):
        '''
        Зашифровывает текст методом Вернама
        '''
        text = list(text)
        key = list(key)
        key_count = 0
        new_text = []
        for i in text:
            try:
                j = key[(key_count%len(key))]
            except ZeroDivisionError:
                key = list(input('Ключ не введен. Введите ключ: '))
                j = key[(key_count%len(key))]
                #print('Введите ключ')
            i = ord(i)
            i += ord(j)
            i = chr(i)
            key_count += 1
            new_text.append(i)


        new_text = ''.join(new_text)
        return new_text

#text = 'Я текст. Сегодня меня будут зашифровывать и расшифровывать.'
#text = ''
#a = Enigma()
#a.encript_by_key_name(text, '')
#a.encrypt_by_number(text, 1)
