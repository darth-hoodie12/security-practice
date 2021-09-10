"""
Create on 10.09.2021
@author Jamie Joly
@file caesar.py
@detail Decoding & Encoding using Caesar Cipher
화이트 해커를 위한 암호화 해킹 Chapter 1
"""

#flag
ENC = 0
DEC = 1

# Make Alberti Cipher makeDisk
# parameter key is Cipher Key(Alphabet)
# if k is alphabet return decDisk
# else return None
def makeDisk(key):
    keyTable = map(lambda x:(chr(x + 65), x), range(26))

    key2index = {}
    for k in keyTable:
        alphabet, index = k[0], k[1]
        key2index[alphabet] = index

    if key in key2index:
        k = key2index[key]
    else:
        return None, None

    encDisk = {}
    decDisk = {}

    for i in range(26):
        enc_i = (i + k) % 26
        enc_ascii = enc_i + 65
        encDisk[chr(i + 65)] = chr(enc_ascii)
        decDisk[chr(enc_ascii)] = chr(i + 65)

    return encDisk, decDisk

# encode and decode by disk
# parameter msg is string, key is Cipher key mode is encode or decode
# return string result of encoding or decoding
def caesar(msg, key, mode):
    ret = ''

    msg = msg.upper()
    encDisk, decDisk = makeDisk(key)

    if encDisk is None:
        return ret

    if mode is ENC:
        disk = encDisk
    elif mode is DEC:
        disk = decDisk
    else:
        return ret

    for c in msg:
        if c in disk:
            ret += disk[c]
        else:
            ret += c

    return ret


def main():
    plaintext = 'abcdefghijklmnopqrstuvwxyz'
    key = 'F'

    print("PlainText -\t%s" %plaintext.upper())
    ciphertext = caesar(plaintext, key, ENC)
    print('Caesar Cipher -\t%s' %ciphertext)
    deciphertext = caesar(ciphertext, key, DEC)
    print('Deciphered -\t%s' %deciphertext)

if __name__ == '__main__':
    main()
