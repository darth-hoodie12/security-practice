#! /usr/bin/python

"""
Create on 18.09.2021
@author Jamie Joly
@file aesForFile.py
@detail using AES library
encrypt and decrypt file
I modified 3desForFile.py so there are same notes
CBC mode
화이트 해커를 위한 암호화 해킹 Chapter 2
"""

# import 3DES module
from Crypto.Cipher import AES
# Crypto.Hash.SHA256 makes ciperkey and initialization vector for 3DES
from Crypto.Hash import SHA256 as SHA
from os import path
KSIZE = 1024


class myAES():
    # No matter how long keytext is, SHA256 hash make proper key length for 3DES
    # parameter keytext is string for creating 3DES cipher key
    #   ivtext is string for initialization vector
    def __init__(self, keytext, ivtext):
        hash = SHA.new() # make new SHA256 object
        # hash.update don't get UNICODE parameter
        # need to encode unicode(string) to utf-8(byte stream)
        # update sha256 hash using parameter "keytext"
        hash.update(keytext.encode('utf-8'))
        # extract hash value by using hash.digest
        # size of key is 256 bit
        key = hash.digest()
        # key of 3DES needs 16 or 24 byte size
        # slicing key size into 24 byte for key of 3DES
        self.key = key[:16]

        # CBC mode needs initialization vector
        # make hash for initialization vector
        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        # init vector value is 8byte from the begining of iv
        self.iv = iv[:16]

    def makeEncInfo(self, filename):
        fillerLen = 0
        fileSize = path.getsize(filename)

        if fileSize % 16 != 0:
            fillerLen = 16 - (fileSize % 16)

        filler = '0' * fillerLen
        header = '%d' %(fillerLen)
        gap = 16 - len(header)
        header += '#' * gap

        return header, filler

        # encryption plaintext using 3DES
        # parameter
        # return
    def enc(self, filename):
        encfilename = 'AES' + filename + '.enc'
        header, filler = self.makeEncInfo(filename)
            # parameter (cipher key, operation mode, initialization vector)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)

        h = open(filename, 'rb')
        hh = open(encfilename, 'wb+')

        enc = header.encode('utf-8')

        content = h.read(KSIZE)
        content = enc + content

        while content:
            if len(content) < KSIZE:
                content += filler.encode('utf-8')
            enc = aes.encrypt(content)
            hh.write(enc)
            content = h.read(KSIZE)

        h.close()
        hh.close()

        # don't using single object des3 for enc() and dec()
        # create different object each fuction
        # decryption ciphertext
    def dec(self, encfilename):
        filename = encfilename + '.dec'
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)

        h = open(filename, 'wb+')
        hh = open(encfilename, 'rb')

        #read header
        content = hh.read(16)
        dec = aes.decrypt(content)
        header = dec.decode()
        fillersize = int(header.split('#')[0])

        #read ciphertext
        content = hh.read(KSIZE)
        while content:
            dec = aes.decrypt(content)
            if len(dec) < KSIZE:
                if fillersize != 0:
                    dec = dec[:-fillersize]
            h.write(dec)
            content = hh.read(KSIZE)
        h.close()
        hh.close()



def main():
    keytext = 'iamjamie'
    ivtext = '1234'
    filename = 'plain.txt'
    encfilename = 'AES' + filename + '.enc'

    myCipher = myAES(keytext, ivtext)
    ciphered = myCipher.enc(filename)
    deciphered = myCipher.dec(encfilename)

if __name__ == '__main__':
    main()
