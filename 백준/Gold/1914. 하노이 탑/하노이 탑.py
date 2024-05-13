import sys,io
input = sys.stdin.readline
output = io.StringIO()
d = {}
a = int(input())
def move(a, b, c):
    if a == 1:
        return f'{b} {c}\n' 
    if (a, b) in d:
        return d[(a, b)]  
    d[(a, b)] = ''.join([move(a-1, b, 6-b-c), f'{b} {c}\n', move(a-1, 6-b-c, c)])
    return d[(a, b)]
output.write(f'{(1<<a)-1}\n')
if a <= 20:
    output.write(f'{move(a, 1, 3)}')
sys.stdout.write(output.getvalue())