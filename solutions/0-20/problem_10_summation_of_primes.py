"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""
from decorators_k import writeResult
import sys
sys.path.insert(0, "..")

@writeResult
def solution(x=None):
    lst = [False, False] + [True for i in range(x)]
    res = 0
    for i in range(2, x - 1):

        if lst[i]:
            for j in range(i + i, x - 1, i):
                lst[j] = False

            res += i
    return res

solution(2000000)

## result: 142913828922. Time: 0.9396259784698486