"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""
from decorators_k import writeResult
from functools import reduce
import sys
sys.path.insert(0, "..")


@writeResult
def solution(x=None):
    return reduce(lambda a, b: a + b, sorted(list(set(list(range(0, x, 5)) + list(range(0, x, 3))))), 0)


solution(1000)

## result: 233168. Time: 0.0
