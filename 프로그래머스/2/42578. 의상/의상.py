from collections import Counter
from functools import reduce
def solution(clothes):
    c = Counter(x[1] for x in clothes)
    mult = reduce(lambda a,c:a*(c+1),c.values(),1)
    return mult-1