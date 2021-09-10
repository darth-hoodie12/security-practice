# -*- coding: utf-8 -*-
"""
Create on 07.09.2021
@author Jamie Joly git @darth-hoodie12
@file first_encryptor.py
@detail Decoding & Encoding using Le Grand Code
화이트 해커를 위한 암호화 해킹 Chapter 1
"""

# 책에서 변형한 르그랑 코드북 구성
# parameter None
# return Codebook for Encryption, Codebook for Decryption
def makeCodeBook():
    decBook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h',
                '6':'i', '0':'l', '9':'m', '*':'n', '%':'o', '=':'p', '(':'r',
                ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}

    encBook = {}
    for i in decBook:
        val = decBook[i]
        encBook[val] = i

    return encBook, decBook

# Encrypting
# parameter string _msg is plaintext, string encBook is encryption Codebook
# return ciphertext
def encrypt(_msg, encBook):

    msg = _msg
    for i in msg:
        if i in encBook:
            msg = msg.replace(i, encBook[i])

    return msg

# Decrypting
# parameter string _msg is ciphertext, string decBook is decryption makeCodeBook
# return plaintext
def decrypt(_msg, decBook):
    msg = _msg
    for i in msg:
        if i in decBook:
            msg = msg.replace(i, decBook[i])

    return msg

if __name__ == '__main__':
    plainText = 'I love you with all my heart'
    print("------원문------")
    print(plainText)

    encBook, decBook = makeCodeBook()
    cipherText = encrypt(plainText, encBook)
    print("\n------암호화-------")
    print(cipherText)

    decipherText = decrypt(cipherText, decBook)
    print("\n------복호화-------")
    print(decipherText)
