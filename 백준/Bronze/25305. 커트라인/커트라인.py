N,k=map(int,input().split())
*X, = map(int,input().split())
X.sort(reverse=True)
print(X[k-1])