"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
from decorators_k import writeResult
import sys
sys.path.insert(0, "..")

@writeResult
def solution(x=None):
    c = 3
    prime_list = [2]
    while len(prime_list) < x:
        y = c**0.5
        for i in prime_list:
            if c % i == 0:
                break
            elif i > y:
                prime_list.append(c)
                break

        c += 2
    return prime_list[-1]

solution(10001)

## result: 104743. Time: 0.22514986991882324