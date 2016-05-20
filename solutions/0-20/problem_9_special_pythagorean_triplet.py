"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
 a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc."""
from decorators_k import writeResult
import sys
sys.path.insert(0, "..")

@writeResult
def solution(x=None):
    c = 499
    count_iter = 0
    while c > 1:
        b = c
        while b > 1:
            b -= 1
            a = 1000 - c - b
            if not a < b:
                continue
            if not a % 4 == 0 or b % 4 == 0:  # a (xor) b divide 4
                continue
            d = ((c - a)*(c - b)/2)**0.5
            if not d == int(d):
                continue
            count_iter += 1
            if a**2 + b**2 == c**2:
                print("GJ, a=", a, " ,b=", b, " ,c=", c)
                return a * b * c

        c -= 2  # only odd

solution()

## result: 31875000. Time: 0.007005214691162109