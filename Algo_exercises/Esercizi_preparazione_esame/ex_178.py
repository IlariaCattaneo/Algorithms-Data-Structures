def algo_x(A):
    i = 0
    j = len(A)
    while i < j:
        if A[i] % 2 == 0:
            j -= 1
            v = A[i]
            algo_y(A,i,j)
            A[j] = v
        else:
            i += 1
    return j

def algo_y(A,p,q):
    while p < q:
        A[p] = A[p+1]
        p += 1

# algo_x sorts the elements of A such that we have even numbers on the right and odd numbers on the left

def better_algo_x(A):
    i = 0
    j = len(A)
    while i < j:
        if A[i] % 2 == 0:
            j -= 1
            A[i], A[j] = A[j], A[i]
        else: 
            i += 1
    return j