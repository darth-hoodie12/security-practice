# -*- coding: utf-8 -*-
"""
Create on 10.09.2021
@author Jamie Joly
@file first_fileEncryptor.py
@detail Decoding & Encoding using Le Grand Code
화이트 해커를 위한 암호화 해킹 Chapter 1
"""

# import functions from first_encryptor.py file
import first_encryptor as fe

# read plaintext from .txt and encrypt plaintext
# return encryption .txt file
if __name__ == '__main__':
    h = open('plain.txt', 'rt')
    content = h.read()
    h.close()

    encbook, decbook = fe.makeCodeBook()
    content = fe.encrypt(content, encbook)

    h = open('encryption.txt', 'wt+')
    h.write(content)
    h.close()
