"""The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million."""
from decorators_k import writeResult
import sys
sys.path.insert(0, "..")

@writeResult
def solution(x=None):
    term_cnt = 0
    max_val = 1
    result = {}
    for i in range(1, x + 1):
        temp_cnt = 1
        num = i
        while num != 1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3 * num + 1
            temp_cnt += 1
            if num in result:
                temp_cnt += result[num]
                break

        result[i] = temp_cnt

        if temp_cnt > term_cnt:
            term_cnt = temp_cnt
            max_val = i
    return max_val

solution(1000001)

## result: 837799. Time: 4.325884103775024