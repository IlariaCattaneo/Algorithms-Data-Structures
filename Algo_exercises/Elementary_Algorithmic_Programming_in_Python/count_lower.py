def count_lower(A,x):
    counter = 0
    for i in range(len(A)):
        if A[i] < x:
            counter += 1
    return counter

# Ex 1
print(count_lower([0,7,10,-2,3], 7))

# Ex 2
print(count_lower([3, 2, 1, 1, 3, 2, 2, 3, 1], 2))

# Ex 3
print(count_lower([3, 2, 1, 1, 3, 2, 2, 3, 1], 10))

# Ex 4
print(count_lower([], 1000000000000000))

# Ex 5
print(count_lower([2, 3, 4, 5], 1))