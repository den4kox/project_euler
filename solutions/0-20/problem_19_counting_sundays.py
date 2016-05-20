"""You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
from decorators_k import writeResult
import sys
sys.path.insert(0, "..")


@writeResult
def solution(x = None):
    count = 0
    for y in range(1900 ,2001):
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            print("Высокосный: ", y,"y % 400 = ",y % 400)
            year = [list(range(1, 32)),
                    list(range(1, 30)),
                    list(range(1, 32)),
                    list(range(1, 31)),
                    list(range(1, 32)),
                    list(range(1, 31)),
                    list(range(1, 32)),
                    list(range(1, 32)),
                    list(range(1, 31)),
                    list(range(1, 32)),
                    list(range(1, 31)),
                    list(range(1, 32)),]
            print(year)
            return 1
solution()

## result: 1. Time: 0.0009927749633789062