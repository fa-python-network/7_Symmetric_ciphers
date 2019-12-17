'''
Тут будет тело программы
'''

class Enigma_killer():

    #def most_frequent(self,text):
    #    return max(set(text), key=text.count)

    def decript_by_number(self, text):
        '''
        Расшифровывает текст зашифрованный методом Цезаря
        '''

        text = list(text)
        new_text = []
        new_sym = max(set(text), key=text.count)
        expect_key = ord(new_sym) - ord(' ')
        for i in text:
            i = ord(i)
            print(i)
            i -= int(expect_key)
            i=chr(i)
            new_text.append(i)
        new_text = ''.join(new_text)
        return new_text

    def decript_by_key_name(self,text):
        '''
        Расшифровывает тест зашифрованный методом Вернама
        '''




    #def decript_by_key_name(self, text, key):

#text = 'а!ужлту/!Тждпеоѐ!нжоѐ!вфефу!ибщйхспгьгбуэ!й!сбтщйхспгьгбуэ/'
#a = Enigma_killer()
#a.decript_by_number(text)
