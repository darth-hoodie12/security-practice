#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:22:41 2021

@author: jamiejoly
"""

import enc

def decryption():
    print('Decryption!')
    
if __name__ == '__main__':
    print('dec.py is main!')
    enc.encryption()
    decryption()
else:
    print('dec.py is imported from other module!')