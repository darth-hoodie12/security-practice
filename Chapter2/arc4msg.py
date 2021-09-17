"""
Create on 18.09.2021
@author Jamie Joly
@file arc4msg.py
@detail using ARC4 Library
for Stream Cipher
ECB mode
화이트 해커를 위한 암호화 해킹 Chapter 2
"""

from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256 as SHA

class myARC4():
    def __init__(self, keytext):
        self.key = keytext.encode()


    def enc(self, plaintext):
        arc4 = ARC4.new(self.key)
        encmsg = arc4.encrypt(plaintext.encode())

        return encmsg

    def dec(self, ciphertext):
        arc4 = ARC4.new(self.key)
        decmsg = arc4.decrypt(ciphertext)

        return decmsg

def main():
    keytext = 'iamjamie'
    msg = 'python3x'

    myCipher = myARC4(keytext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)

    print('ORIGINAL:\t%s' %msg)
    print('CIPHERED:\t%s' %ciphered)
    print('DECIPHERED:\t%s' %deciphered)

if __name__ == "__main__":
    main()
