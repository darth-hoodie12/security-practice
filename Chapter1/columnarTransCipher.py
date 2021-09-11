"""
Create on 11.09.2021
@author Jamie Joly
@file caesar.py
@detail Decoding & Encoding using Columnar Transposition Cipher
화이트 해커를 위한 암호화 해킹 Chapter 1

did not work
"""
ENC = 0
DEC = 1

# parse cipher key and make encode, decode tables
# parameter _key is cipher key
# return encode, decode table
def parseKey(_key):

    key = _key
    tmp = []

    for i, k in enumerate(key):
        tmp.append((i, k))

    sortedKey = sorted(tmp, key = lambda x:x[1])

    encTable = {}
    decTable = {}

    for i, r in enumerate(sortedKey):
        encTable[r[0]] = i
        decTable[i] = r[0]

    return encTable, decTable

def encoding(_keylen, _msg, table):

    len = _keylen
    msg = _msg
    ciphertext = ''

    buf = [''] * len
    for i, c in enumerate(msg):
        col = i % len
        index = table[col]
        buf[index] += c

    for text in buff:
        ciphertext += text

    return ciphertext

def decoding(_keylen, _msg, table):

    len = _keylen
    msg = _msg

    plaintext = ''
    buf = ['']*len
    blockSz = int(len(msg)/len)
    st = 0

    for i in range(len):
        text = msg[st:st+blockSz]
        index = table[i]
        buf[index] += text
        st += blockSz

    for i in range(blockSz):
        for j in range(len):
            if buf[j][i] != '0':
                plaintext += buf[j][i]

    return plaintext

# analysis cipherkey and make text calculate easier
# parameters key is input cipherkey msg is input text mode is choose enc or dec
# return
def transposition(_key, _msg, mode):

    msg = _msg.upper()
    key = _key.upper()

    encTable, decTable = parseKey(key)

    keyLen = len(key)
    msgLen = len(msg)

#   if msgLen % keyLen != 0:
#       filler = '0'*(keyLen - (msgLen % keyLen)
#   msg += filler

    if msgLen % keyLen != 0:
        r = keyLen - (msgLen % keyLen)
        for i in range(r):
            msg += '0'

    if mode is ENC:
        table = encTable
        return encoding(keyLen, msg, table)

    elif mode is DEC:
        table = decTable
        return decoding(keyLen, msg, table)


def main():

    cipherKey = input("Input Cipher Key : ")
    inputText = input("Input plain or cipher Text : ")
    mode = input("If you want encode enter 0, else if decode enter 1 : ")
    print(transposition(cipherKey, inputText, mode))

    return 0

if __name__ == '__main__':
    main()
