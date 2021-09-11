"""
Create on 11.09.2021
@author Jamie Joly
@file caesar.py
@detail Decoding & Encoding using Affine Cipher
화이트 해커를 위한 암호화 해킹 Chapter 1
"""

#flag
ENC = 0
DEC = 1

# Make Alberti Cipher disk
# parameter k1, k2 are Cipher Keys
# return decDisk & encDisk
def makeDisk(k1, k2):

    encDisk = {}
    decDisk = {}

    for i in range(26):
        enc_i = (k1 * i + k2) % 26
        enc_ascii = enc_i + 65
        encDisk[chr(i + 65)] = chr(enc_ascii)
        decDisk[chr(enc_ascii)] = chr(i + 65)

    return encDisk, decDisk

# encode and decode by disk
# parameter msg is string | key1, key2 are Cipher keys
# paramode is encode or decode
# return string result of encoding or decoding
def affine(msg, key1, key2, mode):
    ret = ''

    msg = msg.upper()
    encDisk, decDisk = makeDisk(key1, key2)


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
    key1 = 3 # This value is comprime of key2
    key2 = 5 # This value is the number of alphabet(English)

    print("PlainText -\t%s" %plaintext.upper())
    ciphertext = affine(plaintext, key1, key2, ENC)
    print('Affine Cipher -\t%s' %ciphertext)
    deciphertext = affine(ciphertext, key1, key2, DEC)
    print('Deciphered -\t%s' %deciphertext)

if __name__ == '__main__':
    main()
