def compress_sequence(A):
    counter = 1
    for i in range(len(A)-1):
        if len(A) == 1:
            print(A[i])
        if A[i] == A[i+1]:
            counter += 1
        elif A[i] != A[i+1]:
            if counter >= 3:
                print(A[i], '*', counter)
                counter = 1
            else:
                print(A[i])
                counter = 1
    if counter >= 3:
        print(A[i], '*', counter)
    else:
        print(A[i+1])