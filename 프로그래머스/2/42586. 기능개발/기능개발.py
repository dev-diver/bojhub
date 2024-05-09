def solution(progresses, speeds):
    Q = []
    for p,s in zip(progresses,speeds):
        canDeploy = -((p-100)//s)
        if len(Q)==0 or Q[-1][0]<canDeploy:
        	Q.append([canDeploy,1])
        else:
        	Q[-1][1]+=1
    return [q[1] for q in Q]