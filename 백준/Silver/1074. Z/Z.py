N,R,C = map(int, input().split())

k=0
def recur(a,c,n):
    global k
    if(n==0):
        if(a==C and c==R):
            print(k)
            return
        k+=1
        return
    rng = 2**n
    half = rng//2
    if(not (a<=C<a+rng and c<=R<c+rng)):
        k+=rng*rng
        return
    recur(a,c,n-1)
    recur(a+half,c,n-1)
    recur(a,c+half,n-1)
    recur(a+half,c+half,n-1)

recur(0,0,N)