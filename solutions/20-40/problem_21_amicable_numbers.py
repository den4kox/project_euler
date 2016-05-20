"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000."""
from math import sqrt

from decorators_k import writeResult
import sys
sys.path.insert(0, "..")


def dn(x):
    m = [1]
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            m.extend([i,int(x/i)])
    return sum(set(m))


@writeResult
def solution(x=None):
    res = []
    for i in range(1, x):
        a = dn(i)
        b = dn(a)
        if i == b:
            if i != a:
                res.extend([a, i])
    return sum(set(res))
solution(10000)

## result: 31626. Time: 0.31934642791748047