def position_in_sequence(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1
