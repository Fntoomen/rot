from rot import decrypt as dec
from rot import chars
from sys import argv
from collections import Counter

def brkc(m: str, f: str, x: int):
    t=tuple(open(f).read().splitlines()[:x])
    decm=[]
    for i in range(1, len(chars)):
        decmsg=dec(m, i)
        print(f"{i}: {decmsg}")
        for x in t:
            if x.upper() in decmsg:
                decm.append(decmsg)
    return Counter(decm)

if __name__ == "__main__":
    try:
        a=argv[1]
        b=argv[2]
        c=int(argv[3])
    except IndexError:
        a=input("Give encoded text to break: ")
        b=input("Give filename of file which contains wordlist: ")
        c=int(input("Type how many words to read from the wordlist ('-1'=every): "))
    print(brkc(a, b, c))
