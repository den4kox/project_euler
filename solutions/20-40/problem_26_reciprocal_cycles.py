"""A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2= 0.5
1/3= 0.(3)
1/4= 0.25
1/5= 0.2
1/6= 0.1(6)
1/7= 0.(142857)
1/8= 0.125
1/9= 0.(1)
1/10= 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
import math
from collections import Counter
from decorators_k import writeResult
from decimal import getcontext, Decimal

import sys
sys.path.insert(0, "..")

def remNull(x):
    for i, n in enumerate(x):
        if n != "0":
            return x
        x = x[1:]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

@writeResult
def solution(x=None):
    getcontext().prec = 5000
    len_ = 0
    nubme = 0
    qwe = ""
    for n in range(2, x):
        c = Decimal(1) / Decimal(n)

        text = remNull(str(c)[2:])
        if len(text) < 11 or len(Counter(text)) < 5 :
            continue
        l = len(str(c))-2
        #print(n, text)
        for yt in range(0,100):
            list_index = find(text, text[yt])
            if len(list_index)<4:
                continue
            #print(list_index[1], list_index[0])
            len_res = list_index[1]-list_index[0]
            if len_ > len_res:
                continue
            #print(text[list_index[0]:])
            if text[list_index[0]:list_index[0]+900] == text[list_index[1]:list_index[1]+900]:

                qwe = text
                nubme = n
                len_ = len_res
    return (nubme, len_)
solution(1001)


## result: (831, 69). Time: 70.13785219192505