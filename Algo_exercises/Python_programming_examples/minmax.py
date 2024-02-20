def minmax(A):
    min = A[0]
    max = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
        elif A[i] > max:
            max = A[i]
    return min, max

print(minmax([10, 15, 7, 9, 1, 3]))