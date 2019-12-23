def enc(k, m):
    new_m = ''
    for ch in m:
        if ord(ch) > 65525:
            ch = ord(ch) - 65525 + k
            new_m += chr(ch)
        else:
            ch = ord(ch) + k
            new_m += chr(ch)
    return new_m


def dec(k, new_m):
    m = ''
    for ch in new_m:
        if ord(ch) > 65525:
            ch = ord(ch) - 65525 - k
            m += chr(ch)
        else:
            ch = ord(ch) - k
            m += chr(ch)
    return m


def hack(m):
    often_char = ''
    max_fre = -1
    for i in m:
        if m.count(i) > max_fre:
            max_fre = m.count(i)
            often_char = i
    key_secret = ord(often_char) - 32
    secret = ''
    for i in m:
        if ord(i) > 65525:
            ch = ord(i) - 65525 - key_secret
            secret += chr(ch)
        else:
            ch = ord(i) - key_secret
            secret += chr(ch)
    return secret


msg = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore ' \
      'magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo ' \
      'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla ' \
      'pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id ' \
      'est laborum. '

key = int(input('input the key: '))
msg_enc = enc(key, msg)

# print('in: ' + msg_enc)
# msg_dec = dec(key, msg_enc)

msg_hck = hack(msg_enc)
print('hack out : ' + msg_hck)
