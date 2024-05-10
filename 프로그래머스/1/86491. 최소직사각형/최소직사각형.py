def solution(sizes):
    answer = 0
    sizes = [(max(x), min(x)) for x in  sizes]
    mxWidth = 0
    mxHeight = 0
    for width, height in sizes:
        mxWidth = max(width, mxWidth)
        mxHeight = max(height,mxHeight)
    return mxWidth*mxHeight