def maximal_regular_sequence(A):
    count = 0
    for i in range(1,len(A)):
        if A[i] > A[i-1]:
            count += 1
    return count

print(maximal_regular_sequence([14, 22, 5, 16, 10, 34, 35, 23, 51, 28, 0]))