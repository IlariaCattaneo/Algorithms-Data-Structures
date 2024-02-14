def sort(A, n):
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                # 1 = ascending
                if n == 1:
                    A[i], A[j] = A[j], A[i]
            elif A[i] < A[j]:
                # 0 = descending
                if n == 0:
                   A[i], A[j] = A[j], A[i] 
    return A
