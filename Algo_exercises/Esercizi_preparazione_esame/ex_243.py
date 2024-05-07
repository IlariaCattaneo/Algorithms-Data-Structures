def rotate_in_place(A,k):
    if k == 0:
        return A
    for i in range(k):
        j = 0
        i = 1
        while i < len(A) and j < len(A)-1:
            A[j], A[i] = A[i], A[j]
            j += 1
            i += 1
    return A