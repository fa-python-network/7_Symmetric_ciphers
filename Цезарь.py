from collections import defaultdict


def decrypt(word: str or list) -> str:
    

    counter = defaultdict(int)
    key, j = "", 0
    for i in word:
        counter[i] += 1
        if counter[i] > j:
            key, j = i, counter[i]
    return chr(ord(key) - ord(" "))


def encryption(word: str, key: str, decode: bool = False, clen: int = 65536) -> str:
   

    if len(key) != 1:
        raise ValueError

    return "".join(chr((ord(i) - ord(key) if decode else (ord(i) + ord(key))) % clen) for i in word)


if __name__ == '__main__':

    text = "I Really Nedd Points"
    key = "Я"

    encrypted_text = encryption(text, key)
    decrypted_text = encryption(encrypted_text, key, decode=True)

    print(f"{text} -> «{encrypted_text}» -> {decrypted_text}")

    print(f"Подобранный ключ: {decrypt(encrypted_text)}")