
import random

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main():
    vector = "Happy new year"
    encrypted = encrypt(vector)
    decrypted = decrypt(encrypted[0], encrypted[1])

    print("Test Vector: " + vector)
    print("OTP: " + encrypted[0])
    print("Encrypted: " + encrypted[1])
    print("Decrypted: " + decrypted)


def encrypt(plaintext):

    otp = "".join(random.sample(charset, len(charset)))
    result = ""

    for c in plaintext.upper():
        if c not in otp:
            continue
        else:
            result += otp[charset.find(c)]

    return otp, result


def decrypt(otp, secret):

    result = ""

    for c in secret.upper():
        if c not in otp:
            continue
        else:
            result += charset[otp.find(c)]

    return result


if __name__ == "__main__":
    main()