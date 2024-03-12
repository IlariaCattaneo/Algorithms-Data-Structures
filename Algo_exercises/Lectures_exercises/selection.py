import random

def selection(A, k):
    L = []
    R = []
    M = []
    v = random.choice(A)
    for a in A:
        if a < v:
            L.append(a)
        elif a > v:
            R.append(a)
        else:
            M.append(a)
    if len(L) > k:
        return selection(L, k)
    if len(L) + len(M) <= k:
        return selection(R, k - len(L) - len(M))
    return v