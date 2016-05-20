"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""
from decorators_k import writeResult
import sys
sys.path.insert(0, "..")

units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

scales = ["hundred", "thousand", "million", "billion", "trillion"]

def before100(x):
    res = 0
    for n in range(1,x+1):
        if n <= len(units)-1:
            res += len(units[n])
            continue
        if x < 100:
            s = str(n)
            res += len(units[int(s[-1])]) + len(tens[int(s[-2])])
            continue
    return res

@writeResult
def solution(x = None):
    r = before100(99)
    if 1001 > x > 99:
        r *= 10
        for n in range(1,10):
            r += len(units[n]) + len(scales[0])
            r += 99*(len(units[n]) + len(scales[0]) + 3)
    return r + len(units[1]) + len(scales[1])
                

solution(1000)

## result: 21124. Time: 0.0