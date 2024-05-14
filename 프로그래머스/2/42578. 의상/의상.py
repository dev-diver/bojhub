from collections import Counter
from functools import reduce
from operator import mul
def solution(clothes):
    c = Counter(x[1] for x in clothes)
    m = reduce(mul,[c[e]+1 for e in c])
    return m-1