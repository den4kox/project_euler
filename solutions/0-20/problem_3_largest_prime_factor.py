"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""
import sys
sys.path.insert(0, "..")
from decorators_k import writeResult
from math import sqrt


@writeResult
def solution(x=None):
    res = []
    for n in range(2, int(sqrt(x) + 1)):
        if x % n == 0:
            # print(n)
            for y in range(2, int(sqrt(n) + 1)):
                if n % y == 0:
                    break

            else:
                res.append(n)
    return res


solution(600851475143)

## result: [71, 839, 1471, 6857]. Time: 0.13108611106872559