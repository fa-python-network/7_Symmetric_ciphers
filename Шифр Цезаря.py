from collections import defaultdict


def decrypt(word: str or list) -> str:
    """
    Находит ключ для текста
    Более медленный, однострочный вариант:
    return chr(ord(Counter(word).most_common(1)[0][0]) - ord(" "))

    :param word:
    :return:
    """

    counter = defaultdict(int)
    key, j = "", 0
    for i in word:
        counter[i] += 1
        if counter[i] > j:
            key, j = i, counter[i]
    return chr(ord(key) - ord(" "))


def encryption(word: str, key: str, decode: bool = False, clen: int = 65536) -> str:
    """
    Шифрует текст ключем

    :param word: Слово которе требутся расшифровать/зашифровать
    :param key: Ключ
    :param decode: Если требутся расшифровать True
    :param clen: Длина кодировки
    :return:
    """

    if len(key) != 1:
        raise ValueError

    return "".join(chr((ord(i) - ord(key) if decode else (ord(i) + ord(key))) % clen) for i in word)


if __name__ == '__main__':

    text = "I Love Python"
    key = "Я"

    encrypted_text = encryption(text, key)
    decrypted_text = encryption(encrypted_text, key, decode=True)

    print(f"{text} -> «{encrypted_text}» -> {decrypted_text}")

    print(f"Подобранный ключ: {decrypt(encrypted_text)}")
