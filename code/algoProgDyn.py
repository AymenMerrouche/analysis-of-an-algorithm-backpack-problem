import math
def algoProgDyn(K, V, S, M):
    if S < 0: return math.inf
    if M[S][K] >= 0: return M[S][K]
    if S == 0:
        M[S][K] = 0
        return M[S][K]
    if K == 0:
        M[S][K] = math.inf
        return M[S][K]
    op1 = algoProgDyn(K-1, V, S, M)
    op2 = algoProgDyn(K, V, S - V[K], M) + 1
    mini = min(op1, op2)
    M[S][K] = mini
    return mini


def backward(S, K, V, M):
    A=[0]*(K+1)
    cpt=0
    SE=S
    while K>1:
        if M[SE][K]<M[SE][K-1]:
            while (SE-V[K]>=0)and M[SE-V[K]][K]+1 < M[SE][K-1]:
                A[K]+=1
                SE-=V[K]
                cpt+=V[K]
        K-=1
    A[1]=S-cpt
    return A
