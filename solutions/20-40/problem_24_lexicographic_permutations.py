"""A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
from functools import reduce

from decorators_k import writeResult
import sys
sys.path.insert(0, "..")

lst = [0, 1, 2,3,4,5,6,7,8,9]

def fact(x):
    return reduce(lambda ac, x: ac*x, range(1, x+1), 1)
print(fact(9))

import itertools
print([x for x in itertools.islice(itertools.permutations([0,1,2,3,4,5,6,7,8,9],10),999999,1000000)])

@writeResult
def solution(x=None):


    for n in range(1,1000000):
        
        for i in range(-2, -11, -1):
            if x[i] < x[i+1]:
                l = 9
                while x[i] >= x[l]:
                    l -= 1
                x[i], x[l] = x[l], x[i]
                x = x[:i+1] + list(reversed(x[i+1:10]))

                break

        
    return ''.join(str(n) for n in x)

solution(lst)

## result: 2783915460. Time: 3.9580538272857666