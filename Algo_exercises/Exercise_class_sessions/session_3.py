def array_remove_pos(A, i):
    if A[i] == A[len(A)-1]:
        A.pop()
    else:
        A[i], A[len(A)-1] = A[len(A)-1], A[i]
        A.pop()

def array_remove_value(A, x):
    i = 0
    while i < len(A):
        if A[i] == x:
            array_remove_pos(A,i)
        else:    
            i += 1

def array_remove_value_stable(A, x):
    j = 0
    for i in range(len(A)):
        if A[i] != x: # we must keep A[i]
            A[j] = A[i] # we are just copying it in the previous position
            j += 1
    for _ in range(j, len(A)):
        A.pop()
