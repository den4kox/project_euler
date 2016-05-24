"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
from math import sqrt

from decorators_k import writeResult
import sys
sys.path.insert(0, "..")


def list_sum_div(limit):
    result = [0] * limit
    for n in range(1, limit):
        for k in range(2*n, limit, n):
            result[k] += n
    return result

@writeResult
def solution(x=None):
    abundant = set()
    res = 0
    for n, s in enumerate(list_sum_div(x)):
        if s > n:
            print(n)
            abundant.add(n)
        for a in abundant:
            if n - a in abundant:
                break
        else:
            res +=n
    return res

solution(28123)


## result: 4179871. Time: 0.7441484928131104