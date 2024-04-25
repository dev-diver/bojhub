import os,io,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
output = io.StringIO()
T=int(input())
ans = []
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = (x1-x2)**2 + (y1-y2)**2
    if(d==0 and r1==r2):
        output.write("-1\n")
    elif(d==(r1+r2)**2 or d==(r1-r2)**2):
        output.write("1\n")
    elif(d<(r1-r2)**2 or d>(r1+r2)**2):
        output.write("0\n")
    else:
        output.write("2\n")
sys.stdout.write(output.getvalue())