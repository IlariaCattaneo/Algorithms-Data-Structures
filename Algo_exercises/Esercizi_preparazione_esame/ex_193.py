def maximal_distance(A):
    if len(A) < 2:
        return 0
    min = A[0]
    max = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
        elif A[i] > max:
            max = A[i]
    return max - min