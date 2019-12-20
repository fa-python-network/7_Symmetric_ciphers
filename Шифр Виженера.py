from itertools import cycle


def encryption(word, key, decode: bool = False, clen: int = 65536) -> str:
    """
    Расшифровывает или зашифровывает текст

    :param word: Слово которе требутся расшифровать/зашифровать
    :param key: Ключ
    :param decode: Если требутся расшифровать True
    :param clen: Длина кодировки
    :return:
    """

    e, d = lambda x: chr((ord(x[0]) + ord(x[1])) % clen), lambda x: chr((ord(x[0]) - ord(x[1]) + clen) % clen)
    return "".join(map(d if decode else e, zip(word, cycle(key))))


if __name__ == "__main__":

    word = "I Love Python"
    key = "Meow"

    encrypted_text = encryption(word, key)
    decrypted_text = encryption(encrypted_text, key, decode=True)

    print(f"{word} -> «{encrypted_text}» -> {decrypted_text}")
