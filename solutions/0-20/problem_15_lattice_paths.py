"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?"""
from decorators_k import writeResult
import sys
sys.path.insert(0, "..")


@writeResult
def solution(x=None):
    last = [[1], [1, 1]]
    counter = 0
    for x in range(1, 2 * x):
        lst = last[-1]
        last.append([1] + list(map(lambda a: sum(a), zip(lst[:-1], lst[1:]))) + [1])
    return last[-1][int((len(last) - 1) / 2)]

solution(20)

## result: 137846528820. Time: 0.0