#! /usr/bin/python

"""
Create on 17.09.2021
@author Jamie Joly
@file aesformsg.py
@detail using AES library
CBC mode
화이트 해커를 위한 암호화 해킹 Chapter 2
"""

from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA

class myAES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        hash.update(ivtext.encode('utf-8'))
        key = hash.digest()
        self.iv = key[:16]


    # make header
    # change plaintext's length to multiple of 16 byte
    # Header consists of number of '0' + '#'
    def makeEnabled(self, plaintext):
        fillerLen = 0
        textLen = len(plaintext)
        if textLen % 16 != 0:
            fillerLen = 16 - (textLen % 16)

        filler = '0' * fillerLen
        header = '%d' %(fillerLen)
        gap = 16 - len(header)
        header += '#' * gap

        return header+plaintext+filler

    def enc(self, plaintext):
        plaintext = self.makeEnabled(plaintext)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        encmsg = aes.encrypt(plaintext.encode())
        return encmsg

    def dec(self, ciphertext):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decmsg = aes.decrypt(ciphertext)

        header = decmsg[:16].decode()
        fillersize = int(header.split('#')[0])
        if fillersize != 0:
            decmsg = decmsg[16:-fillersize]
        else:
            decmsg = decmsg[16:]

        return decmsg

def main():
    keytext = 'iamjamie'
    ivtext = '1234'
    msg = 'python3x3'

    myCipher = myAES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)

    print('ORIGINAL:\t%s' %msg)
    print('CIPHERED:\t%s' %ciphered)
    print('DECIPHERED:\t%s' %deciphered)

if __name__ == '__main__':
    main()
