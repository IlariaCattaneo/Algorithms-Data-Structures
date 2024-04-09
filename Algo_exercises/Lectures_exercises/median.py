def median(A):
    assert len(A) > 0
    B = sorted(A)
    return B[len(B)//2]

import random
def median_k_selection(A):
    assert len(A) > 0
    L, M, R = [], [], []
    v = random.choice(A)
    for i in range(len(A)):
        if A[i] < v:
            L.append(A[i])
        elif A[i] > v:
            R.append(A[i])
        else:
            M.append(A[i])
    if len(L) > len(A)//2:
        return median_k_selection(L)
    if len(L) + len(M) < len(A)//2:
        return median_k_selection(R)
    return v