import sys
i=sys.stdin.readline
l=[]
for _ in range(int(i())):
    c=i().split()
    if c[0]=="add":
        if c[1] in l:
            continue
        else:
            l.append(c[1])
    elif c[0]=="remove":
        if c[1] in l:
            l.remove(c[1])
    elif c[0]=="check":
        sys.stdout.write('1\n' if c[1] in l else '0\n')
    elif c[0]=="toggle":
        if c[1] in l:
            l.remove(c[1])
        else:
            l.append(c[1])
    elif c[0]=="all":
        l=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    elif c[0]=="empty":
        l=[]