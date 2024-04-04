import sys
input = sys.stdin.readline
N,M = map(int, input().split())

def gcd(a,b):
  if(b==0): return a
  return gcd(b,a%b)

if(N<M):
  N,M=M,N

GCD = gcd(N,M)
LCD = N*M//GCD
print(GCD)
print(LCD)
