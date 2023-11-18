N,R,C = map(int, input().split())

k=0
def recur(a,b,c,d):
    global k
    if(a==b): #
        if(a==C and c==R):
            print(k)
            return
        k+=1
        return
    if(not (a<=C<=b and c<=R<=d)):
        k+=(b-a+1)**2
        return
    coHalf = (a+b)//2
    roHalf = (c+d)//2

    recur(a,coHalf,c,roHalf)
    recur(coHalf+1,b,c,roHalf)
    recur(a,coHalf,roHalf+1,d)
    recur(coHalf+1,b,roHalf+1,d)

recur(0,(2**N)-1,0,(2**N)-1)