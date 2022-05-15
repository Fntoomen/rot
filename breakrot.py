from rot import decrypt as dec
from rot import chars
from sys import argv
from collections import Counter

def brkc(m: str, f: str):
    t=tuple(open(f).read().splitlines()[:1000])
    decm=[]
    for i in range(1, len(chars)):
        decmsg=dec(m, i)
        print(f"{i}: {decmsg}")
        for x in range(len(decmsg)):
            for y in range(x, len(decmsg)):
                if decmsg[x:y].lower() in t:
                        decm.append(decmsg)
    return Counter(decm)
if __name__ == "__main__":
    a=argv[1]
    b=argv[2]
    print(brkc(a, b))
