def vertical_histogram(A):
    max = A[0]
    min = A[0]
    for number in range(len(A)):
        if A[number] > max:
            max = A[number]
        elif A[number] < min:
            min = A[number]
    
    for level in range(max, 0, -1):
        print(' '.join('#' if x >= level else ' ' for x in A))

    print('--' * len(A))

    for level in range(-1, min-1, -1):
        print(' '.join('#' if x <= level else ' ' for x in A))

# ex 1
vertical_histogram([7, 3, -2, 10, 5, -3, 3, 5, 8])