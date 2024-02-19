def minimal_sum(A, x):
    sum = 0
    if len(A) == 1 and A[0] == x:
        return True
    elif len(A) == 0:
        return False
    else:
        for i in range(len(A)):
            if A[i] > 0:
                sum += A[i]
                if sum >= x:
                    return True
        return False

# ex 1
print(minimal_sum([], 1))

# ex 2
print(minimal_sum([1], 1))

# ex 3
print(minimal_sum([3, 2], 4))

# ex 4
print(minimal_sum([3, -2], 4))

# ex 5
print(minimal_sum([2, 1, 5, -3, 9, 4], 20))

# ex 6
print(minimal_sum([32,-3,10,7,-4,18,25], 50))

# ex 7
print(minimal_sum([32,-3,10,7,-4,18,25], 94))