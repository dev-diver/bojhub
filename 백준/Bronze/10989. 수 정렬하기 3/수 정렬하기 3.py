import sys
input = sys.stdin.readline
N = int(input())
arr = [0]*10001
for i in range(N):
    arr[int(input())] +=1

for i in range(1,len(arr)):
    while(arr[i]>0):
        print(i)
        arr[i]-=1
    
