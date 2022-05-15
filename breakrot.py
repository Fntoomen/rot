from cesar import decrypt as dec
from cesar import chars
from sys import argv
from collections import Counter

def brkc(m: str, t: tuple):
    decm=[]
    for i in range(1, len(chars)):
        decmsg=dec(m, i)
        print(f"{i}: {decmsg}")
        for x in range(len(decmsg)):
            for y in range(len(decmsg)):
                if decmsg[x:y] in t:
                        decm.append(decmsg)
    return Counter(decm)
a=argv[1]
b=argv[2].split(" ")
print(brkc(a, b))
