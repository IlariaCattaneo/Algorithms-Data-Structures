def is_monotonic(A, i, j):
    assert i <= j and j < len(A)
    direction = 0
    for k in range(i, j):
        if A[k] < A[k+1]:
            if direction == -1:
                return False
            direction = 1
        elif A[k] > A[k+1]:
            if direction == 1:
                return False
            direction = -1
    return True

# ex 1
print(is_monotonic([1,2,3], 0, 2))

# ex 2
print(is_monotonic([1,1,7,7,9], 0, 4))

# ex 3
print(is_monotonic([9,9,5], 0, 2))

# ex 4
print(is_monotonic([6,6,6,6,6,6], 2, 4))

# ex 5
print(is_monotonic([1,1,1,2,1,3], 0, 5))

# ex 6
print(is_monotonic([1,1,1,2,1,3], 0, 3))

# ex 7
print(is_monotonic([3,2,1,3,2,1], 0, 5))

# ex 8
print(is_monotonic([3,2,1,3,2,1], 2, 3))

# ex 9
print(is_monotonic([3,2,1,3,2,1], 2, 4))

# ex 10
print(is_monotonic([3,2,1,3,2,1], 3, 5))

# ex 11
print(is_monotonic([7,4,7], 0, 2))

# ex 12
print(is_monotonic([7,4,7], 1, 2))
