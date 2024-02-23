def find_peak(A):
    x = A[0]
    for number in A:
        if number > x:
            x = number
    return x

# ex 1
print(find_peak([1,2,3]))

# ex 2
print(find_peak([1,2,7,8,9]))

# ex 3
print(find_peak([9,6,5]))

# ex 4
print(find_peak([1,2,1,-3]))

# ex 5
print(find_peak([1,2,1,0,-3]))

# ex 6
print(find_peak([1,2,3,2,1]))

# ex 7
print(find_peak([1,2,3,4]))

# ex 8
print(find_peak([1,2]))

# ex 9
print(find_peak([4,7,4]))

# ex 10
print(find_peak([7]))

# ex 11
print(find_peak([7,4]))

# ex 12
print(find_peak([4,7]))