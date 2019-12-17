import unittest
from Enigma import Enigma
from Enigma_killer import Enigma_killer
import random

class Test_Enigma(unittest.TestCase):


    def test_by_number(self):
        test_text = input('Введите текст для проверки: ')
        test_key = random.randint(0,65536)
        print('Выбран слючайный числовой ключ: ',test_key )
        encrypt_text = Enigma.encrypt_by_number(self,test_text,test_key)
        decrypt_text = Enigma_killer.decript_by_number(self,encrypt_text)
        self.assertEqual(decrypt_text,test_text)


if __name__ == '__main__':
    unittest.main()
