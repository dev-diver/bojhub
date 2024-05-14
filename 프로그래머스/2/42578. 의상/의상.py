from collections import Counter
import math
def solution(clothes):
    c = Counter(x[1] for x in clothes)
    product = math.prod(c[p]+1 for p in c)
    return product-1