#!/usr/bin/env python3

from rot import rot
from sys import argv
from collections import Counter

def breakRot(m: str, f: str, x: int):
    t=tuple(open(f).read().splitlines()[:x])
    poss=[]
    for i in range(1, 26):
        msg=rot(m, -i)
        print(f"{i}: {msg}")
        for j in t:
            if j.upper() in msg.upper():
                poss.append(msg)
    counter = Counter(poss)
    return f"\033[1;32m {counter} \033[3;32m"

if __name__ == "__main__":
    try:
        a=argv[1]
        b=argv[2]
        c=int(argv[3])
    except IndexError:
        a=input("Give encoded text to break: ")
        b=input("Give filename of file which contains wordlist: ")
        c=int(input("Type how many words to read from the wordlist ('-1'=every): "))
    print(breakRot(a, b, c))
