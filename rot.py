#!/usr/bin/env python3.10

from string import ascii_lowercase as lc, ascii_uppercase as uc
from sys import argv

def rot(m: str, n: int):
    return m.translate(m.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n]))

if __name__ == "__main__":
    try:
        a=argv[1]
        b=int(argv[2])
    except IndexError:
        a=input("Give text to encode/decode: ")
        b=int(input("Type how many shifts do you want to do: "))
    print(f"Text: {rot(a, b)}")
