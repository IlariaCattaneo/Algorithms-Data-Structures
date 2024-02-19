def minimum(A):
    min = A[0]
    for i in range(1, len(A)):
        if A[i] < min:
            min = A[i]
    return min

# Ex 1
A = [1, 2, 3]
print(minimum(A))

# Ex 2
A = [3, 2, 1]
print(minimum(A))

# Ex 3
A = [100, 2, 55, 4, 3, 2, 67, 3]
print(minimum(A))

# Ex 4
A = [7]
print(minimum(A))