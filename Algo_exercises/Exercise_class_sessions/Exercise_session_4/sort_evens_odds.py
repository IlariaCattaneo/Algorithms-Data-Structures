def sort_evens_odds(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if( A[i] % 2 == 1 and A[j] % 2 == 0):
                A[i], A[j] = A[j], A[i]
            elif( ((A[i] % 2 == 0 and A[j] % 2 == 0) or (A[i]%2==1 and A[j]%2==1)) and A[i] > A[j]):
                A[i], A[j] = A[j], A[i]
    print(A)