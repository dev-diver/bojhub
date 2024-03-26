import sys
input = sys.stdin.readline
max = 0
maxi = 0
for i in range(9):
    n = int(input())
    if max < n : 
        max = n
        maxi = i
print(max)
print(maxi+1)
