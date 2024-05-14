from collections import Counter
from functools import reduce
from operator import mul
def solution(clothes):
    c = Counter(x[1] for x in clothes)
    m = reduce(mul,[v+1 for v in c.values()])
    return m-1