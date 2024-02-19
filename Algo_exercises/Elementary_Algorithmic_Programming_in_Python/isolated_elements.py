def isolated_elements(A):
    if len(A) == 1:
        print(A[0])
    elif len(A) == 2 and A[0] != A[1]:
        print(A[0], A[1])
    else:
        for i in range(1, len(A)-1):
            if i == 1 and A[i-1] != A[i] and A[i] != A[i+1]:
                print(A[i-1], A[i])
            elif i == len(A)-2 and A[i-1] != A[i] and A[i] != A[i+1]:
                print(A[i], A[i+1])
            elif A[i-1] != A[i] and A[i] != A[i+1]:
                print(A[i])
        
            
# ex 1
isolated_elements([])

# ex 2
isolated_elements([1])

# ex 3
isolated_elements([7, 3])

# ex 4
isolated_elements([2, 2])

# ex 5
isolated_elements([2, 2, 3, 2, 3])

# ex 6
isolated_elements([-2, 2, 2, 2, -2])

# ex 7
isolated_elements([1,2,1,2,1,2,1,2])