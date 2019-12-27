def decrypt(word):
    keys = {}
    for letter in word:
        keys[letter] = keys.get(letter, 0) + 1
    key = sorted(keys.items(), key=lambda x: x[1], reverse=True)[0]
    return chr(ord(key[0]) - ord(" "))


def encryption(word, key, decode=False):
    ls = []
    for i in word:
        if decode:
            ls.append(chr((ord(i) - ord(key)) % 65536))
        else:
            ls.append(chr(ord(i) + ord(key) % 65536))
    return "".join(ls)


if __name__ == '__main__':

    text = "I Love UNIX"
    key = "I"

    encrypted_text = encryption(text, key)
    decrypted_text = encryption(encrypted_text, key, decode=True)

    print(f"{text} -> «{encrypted_text}» -> {decrypted_text}")

    print(f"Подобранный ключ: {decrypt(encrypted_text)}")
