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


def period(x):
    i = 0
    period_ = ""
    sub_numerator = 10
    while sub_numerator != 10 or i < 1:

        sub_numerator = (sub_numerator % x) * 10
        i += 1
    return i


def gnt(x):
    for i in range(2, x):
        if i%2 != 0 and i%5 != 0:
            yield i

@writeResult
def solution(x=None):
    len_rest = 0
    num = 0
    for i in gnt(x):
        per = period(i)
        if per > len_rest:
            len_rest = per
            num = i
    return (num ,len_rest)
solution(1001)


## result: (983, 982). Time: 0.023437023162841797