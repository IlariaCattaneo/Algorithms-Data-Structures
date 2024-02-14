def repeated_adjacent_elements(A):
    last_element = None
    for i in range(len(A)-1):
        if(A[i] == A[i-1]):
            counter += 1
        else:
            if counter >= 1:
                print(A[i-1])
            counter = 0
    if counter >= 1:
        print(A[i-1])