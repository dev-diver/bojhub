def solution(brown, yellow):
    bp = brown-4
    n = (bp + int((bp**2-16*yellow)**0.5))//4
    m = (bp - int((bp**2-16*yellow)**0.5))//4
    return [n+2,m+2]