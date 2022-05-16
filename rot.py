#!/usr/bin/env python3

from string import ascii_uppercase as chars
from sys import argv

def encrypt(s: str, i: int):
    enc=""
    for x in range(len(s)):
        for y in range(len(chars)):
            if s[x].upper() == chars[y]:
                enc+=chars[(y+i)%len(chars)]
    return enc

def decrypt(s: str, i: int):
    dec=""
    for x in range(len(s)):
        for y in range(len(chars)):
            if s[x].upper() == chars[y]:
                dec+=chars[(y-i)%len(chars)]
    return dec

if __name__ == "__main__":
    try:
        a=argv[1]
        b=int(argv[2])
    except IndexError:
        a=input("Give text to encode/decode: ")
        b=int(input("Type how many shifts do you want to do: "))
    print(f"Encrypted: {encrypt(a, b)}\nDecrypted: {decrypt(a, b)}")
