def find_equal(A):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return True
    return False