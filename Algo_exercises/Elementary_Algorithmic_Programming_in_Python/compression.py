def compress_sequence(A):
    k = 1
    x = 0
    for i in range(len(A)-1):
        x = A[i]
        if A[i] == A[i+1]:
            k += 2
        else:
            if k > 1:
                print(f'{x} * {k}')
                k = 0
            else:
                print(x)
                k = 0
    
# ex 1
compress_sequence([-1,1,1,1,7,7,7,7,5,5,1,1,4,1])
