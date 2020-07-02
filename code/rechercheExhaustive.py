import math
def rechercheExhaustive(K, V, S):
    if S < 0:
        return math.inf
    else:
        if S == 0:
            return 0
        else:
            NbCont = S
            for i in range(1, K+1):
                x = rechercheExhaustive(K, V, S - V[i])
                if x + 1 < NbCont:
                    NbCont = x + 1
            return NbCont


