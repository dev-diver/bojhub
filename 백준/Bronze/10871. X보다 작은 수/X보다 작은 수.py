N,X = map(int,input().split())
*A, = map(int, input().split())
r=filter(lambda x:x<X,A)
print(*r)