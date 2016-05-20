"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

from decorators_k import writeResult
from functools import reduce
import sys
sys.path.insert(0, "..")


def gcd(a, b):
    """ Euclidean algorithm """
    while b:
        a, b = b, a % b
    return a


@writeResult
def solution(*args):
    print(args)
    return reduce(lambda a, b: a // gcd(a, b) * b, args)


solution(*range(1, 20))

## result: 232792560. Time: 0.0010001659393310547