def sieve(n):
    A = [True]*(n+1)
    A[1] = False
    p = 2
    while p <= n:
        if A[p] == True:
            i = p + p
            while i <= n:
                A[i] = False
                i = i + p
        p = p + 1
    return A

print(sieve(10))
            