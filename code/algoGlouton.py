def algoGlouton(K, V, S, A):
    cpt = 0
    while S > 0:
        A[K] += S // V[K]
        cpt += S // V[K]
        S = S % V[K]
        K -= 1
    return cpt

def testGloutonCompatible(K, V):
    A = [0] * (K+1)
    if K >= 3:
        for S in range(V[3] + 2, V[K] + V[K - 1] - 1):
            for j in range(1, K+1):
                if (V[j] < S) and (algoGlouton(K , V, S, A) > 1 + algoGlouton(K, V, S - V[j], A)):
                    return False
    return True
