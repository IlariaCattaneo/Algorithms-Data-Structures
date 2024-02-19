def isolated_elements(A):
    for i in range(0, len(A)):
        if i == 0:        
            if A[i] != A[i+1]:
                print(A[i])
        elif i == len(A)-1:
            if A[i] != A[i-1]:
                print(A[i])
        else:  
            if A[i] != A[i+1] and A[i] != A[i-1]:
                print(A[i])
    



        