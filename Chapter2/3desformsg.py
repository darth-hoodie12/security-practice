#! /usr/bin/python

"""
Create on 13.09.2021
@author Jamie Joly
@file 3desformsg.py
@detail using 3DES library
CBC mode
화이트 해커를 위한 암호화 해킹 Chapter 2
"""

# import 3DES module
from Crypto.Cipher import DES3
# Crypto.Hash.SHA256 makes ciperkey and initialization vector for 3DES
from Crypto.Hash import SHA256 as SHA


class myDES():
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
        self.key = key[:24]

        # CBC mode needs initialization vector
        # make hash for initialization vector
        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        # init vector value is 8byte from the begining of iv
        self.iv = iv[:8]

        # encryption plaintext using 3DES
        # parameter
        # return
    def enc(self, plaintext):
            # parameter (cipher key, operation mode, initialization vector)
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
            # encryption and return result to encmsg
        encmsg = des3.encrypt(plaintext.encode())
        return encmsg

        # don't using single object des3 for enc() and dec()
        # create different object each fuction
        # decryption ciphertext
    def dec(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        decmsg = des3.decrypt(ciphertext)
        return decmsg

def main():
    keytext = 'samsjang'
    ivtext = '1234'
    msg = 'python3x'

    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)

    print('ORIGINAL:\t%s' %msg)
    print('CIPHERED:\t%s' %ciphered)
    print('DECIPHERED:\t%s' %deciphered)

if __name__ == '__main__':
    main()
