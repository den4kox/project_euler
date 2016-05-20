"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?"""
from decorators_k import writeResult
import sys
from functools import reduce

sys.path.insert(0, "..")


@writeResult
def solution(x=None):
    return reduce(lambda acc, a: acc + int(a), str(2 ** x), 0)


solution(1000)

## result: 1366. Time: 0.0