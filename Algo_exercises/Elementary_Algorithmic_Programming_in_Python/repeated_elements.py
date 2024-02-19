def repeated_adjacent_elements(A):
    counter = 0
    for i in range(0, len(A)-1):
        if A[i] == A[i+1]:
            counter += 1
        else:
            if counter >= 1:
                print(A[i])
            counter = 0
    if counter >= 1:
        print(A[i])

# ex 1
repeated_adjacent_elements([])

# ex 2
repeated_adjacent_elements([1])

# ex 3
repeated_adjacent_elements([1, 2])

# ex 4
repeated_adjacent_elements([3, 3])

# ex 5
repeated_adjacent_elements([1,-1,7,7,-1,7,1,7,7,7,7,2,2])