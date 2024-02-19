def position_in_sequence(A,x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1

# Ex 1
print(position_in_sequence([6, 7, 10, -2, 3], 7))

# Ex 2
print(position_in_sequence([3, 2, 1, 1, 3, 2, 2, 3, 1], 1))

# Ex 3
print(position_in_sequence([], 1))

# Ex 4
print(position_in_sequence([2, 3, 4, 5], 1))

# Ex 5
print(position_in_sequence([2, 3, 4, 5], 2))