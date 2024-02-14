def partition(A,k):
    for i in range(len(A)):
        if A[i] >= k:
            p = i
            break
    
    for i in range(len(A)):
        print(f"i={i}, p={p}, A={A}")
        if A[i] <= k:
            if (i > p):
                A[i], A[p] = A[p], A[i]
                p += 1
    return A