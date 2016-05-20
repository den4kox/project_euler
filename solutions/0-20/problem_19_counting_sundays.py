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
    all_year = []
    for y in range(1900 ,2001):
        year = [list(range(1, 32)),
                list(range(1, 30)) if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else list(range(1, 29)),
                list(range(1, 32)),
                list(range(1, 31)),
                list(range(1, 32)),
                list(range(1, 31)),
                list(range(1, 32)),
                list(range(1, 32)),
                list(range(1, 31)),
                list(range(1, 32)),
                list(range(1, 31)),
                list(range(1, 32))]
        all_year.append(year)
    days = [day for year_item in all_year for days in year_item for day in days]
    day_sun = days[6::7].count(1)-days[6:365:7].count(1)
    return day_sun
solution()
"""best short solution:
    sum([1 for month in range(1,13) for year in range(1901,2001) if date(year,month,1).weekday()==6])
"""


## result: 171. Time: 0.0048830509185791016