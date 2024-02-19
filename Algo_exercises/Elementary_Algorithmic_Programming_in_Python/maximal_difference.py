def maximal_difference(A):
    maxdiff = 0
    if len(A) == 1 or len(A) == 0:
        return 0
    else:
        for e in range(0, len(A)-1):
            for el in range(1, len(A)):
                if abs(A[e] - A[el]) > maxdiff:
                    maxdiff = abs(A[e] - A[el])
        return maxdiff

def efficient_maximal_difference(A):
    min = A[0]
    max = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
        elif A[i] > max:
            max = A[i]
    return max - min


# Ex 1
print(maximal_difference([2, 1, 5, 9, 4, 10, 8]))
print(efficient_maximal_difference([2, 1, 5, 9, 4, 10, 8]))

# Ex 2
print(maximal_difference([1]))
print(efficient_maximal_difference([1]))

# Ex 3
print(maximal_difference([1, 1, 1]))
print(efficient_maximal_difference([1, 1, 1]))

# Ex 4
print(maximal_difference([10,-3, 4, 11, 0, 9]))
print(efficient_maximal_difference([10,-3, 4, 11, 0, 9]))