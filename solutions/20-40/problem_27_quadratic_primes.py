"""Euler discovered the remarkable quadratic formula:
n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000where |n| is the modulus/absolute value of ne.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0."""
from decorators_k import writeResult
import sys

sys.path.insert(0, "..")


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False


    return True


@writeResult
def solution(x=None):
    max_a = 0
    max_b = 0
    count_prime = 0
    list_prime = set()
    list_no_prime = set()

    for a in range(-x, x):
        for b in range(-x, x):
            n = 0
            while True:
               
                res = n ** 2 + a * n + b
                
                if res in list_prime:
                    n += 1
                    continue
                elif res in list_no_prime:
                    break
                elif isPrime(res):

                    list_prime.add(res)

                    n += 1
                    continue
                else:
                    list_no_prime.add(res)
                    
                    break
            if count_prime < n:
                count_prime = n
                max_a = a
                max_b = b

    return max_a * max_b


solution(1000)

## result: -59231. Time: 3.752976179122925