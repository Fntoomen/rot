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
    a=argv[1]
    b=int(argv[2])
    print(encrypt(a, b), decrypt(a, b))
