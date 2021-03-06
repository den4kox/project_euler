"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""
import sys

sys.path.insert(0, "..")
from decorators_k import writeResult


@writeResult
def solution(x=None):
    a, b = 0, 1
    lst = 0
    while 1:
        sumi = a + b
        a = b
        b = sumi
        if b > x:
            break
        # if b % 2 == 0:
        if sumi % 2 == 0:
            lst += sumi

    return lst


solution(4000000)

## result: 4613732. Time: 0.0