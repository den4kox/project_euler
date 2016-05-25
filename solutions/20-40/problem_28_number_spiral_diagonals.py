"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""
from decorators_k import writeResult
import sys

sys.path.insert(0, "..")


@writeResult
def solution(x=None):
    res = 1
    kf = 2
    last = 3

    for i in range(0, int(x/2)):
        print('*********')
        for num in range(last, (last+3*kf)+1, kf):
            print(num)
            res+=num
        else:
            kf += 2
            last = num+kf
    return res

solution(1001)

## result: 669171001. Time: 0.019531965255737305