from collections import Counter

N = 65536


def encrypt_caesar(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))
    och = [(x + k) % N for x in map(ord, m)]
    return ''.join(map(chr, och))


def decrypt_caesar(k, c):
    och = [(x - k) % N for x in map(ord, c)]
    return ''.join(map(chr, och))


def vz(m):
    most = Counter(m).most_common()[0][0]
    key = ord(most) - ord(' ')
    return decrypt_caesar(key, m)


def encrypt_vernam(k, m):
    k = k * (len(m) // len(k)) + k[:(len(m) % len(k))]
    return ''.join(map(chr, [i ^ x for i, x in zip(map(ord, m), map(ord, k))]))


def decrypt_vernam(k, c):
    return encrypt_vernam(k, c)


k = int(input("Enter Caesar's encrypt key: "))
text = "Свобода – это возможность сказать, что дважды два – четыре. Если дозволено это, все остальное отсюда следует."
encrypted_text = encrypt_caesar(k, text)
decrypted_text = decrypt_caesar(k, encrypted_text)
print('Encrypted with Caesar text: ', encrypted_text)
print('Decrypted with Caesar text:', decrypted_text)
k = "1 2 5 4 9 8"
encrypted_text_ver = encrypt_vernam(k, text)
decrypted_text_ver = decrypt_vernam(k, encrypted_text_ver)
print('Encrypted with Vernam text:', encrypted_text_ver)
print('Decrypted with Caesar text:', decrypted_text_ver)