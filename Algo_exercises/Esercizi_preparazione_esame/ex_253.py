def algo_x(A,k):
    B = algo_y(A,0,len(A))
    c = 0
    for i in range(len(B)):
        if i < k:
            c = c + B[i]
        else:
            return c
    return c

def algo_y(A,i,j):
    D = []
    if j - i == 1:
        D.append(A[i])
    elif j - i > 1:
        k = (i + j)//2
        B = algo_y(A,i,k)
        C = algo_y(A,k,j)
        b = 0
        c = 0
        while b < k - i or c < j - k:
            if c >= j - k or (b < k - i and B[b] < C[c]):
                D.append(B[b])
                b = b + 1
            else:
                D.append(C[c])
                c = c + 1
    return D
# algo y is the reproduction of a merge-sort
# algo x returns the sum of numbers until the k-th position, which means the sum of numbers in the first k positions
# worst case complexity is theta(nlogn); algo y is theta(nlogn) which is the complexity of merge-sort and in algo x we scan array B in theta(n), so combining them we take the highest order which is theta(nlogn)
# wcc happens mainly when we do the sorting, which happens quite always
# also best case complexity is theta(nlogn) best the predomincance is given by the merge-sort

def sum(A):
    sum = 0
    for i in range(len(A)):
        s += A[i]
    return sum

import random
def better_algo_x(A,k):
    if k >= len(A):
        return sum(A)
    v = random.choice(A)
    L, M, R = [], [], []
    i = 0
    for i in range(len(A)):
        if A[i] < v:
            L.append(A[i])
        elif A[i] > v:
            R.append(A[i])
        else:
            M.append(A[i])
    if k < len(L):
        return better_algo_x(L,k)
    if k - len(L) <= len(M):
        return sum(L) + (k-len(L))*v
    return sum(L) + sum(M) + better_algo_x(R,k-len(L)-len(M))
# this algo uses the k-selection which is a divide and conquer algorithm
# it works in theta(n^2) in worst case but in theta(n) in both average and best case