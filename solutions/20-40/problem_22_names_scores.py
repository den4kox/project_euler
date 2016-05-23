"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?"""
from functools import reduce

from decorators_k import writeResult
import urllib.request
import sys
sys.path.insert(0, "..")

names = "https://projecteuler.net/project/resources/p022_names.txt"
# with urllib.request.urlopen(names) as url:
#     s = url.read()
# lst = s.decode("utf-8").replace("\"", "").split(",")

def alphabetical(text):
    return reduce(lambda ac, x: ac+ord(x) - 64, text, 0)


@writeResult
def solution(x = None):
    with open('p022_names.txt', 'r') as content_file:
        s = content_file.read()
    return sum([alphabetical(x)*(i+1) for i, x in enumerate(sorted(s.replace("\"", "").split(",")))])
solution(938)

## result: 871198282. Time: 0.015624284744262695