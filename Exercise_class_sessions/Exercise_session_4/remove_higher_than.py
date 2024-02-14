def rht(A, n):
    B = []
    for i in range(len(A)):
        c = 0
        for j in range(len(A)):
            if A[i] == A[j]:
                c += 1
        if c <= n:
            B.append(A[i])
    return B