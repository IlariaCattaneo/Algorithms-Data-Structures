def full_adder(a,b,c):
    # return a pair (s,c)
    if a == 0 and b == 0 and c == 0:
        return (0,0)
    if a == 1 and b == 1 and c == 1:
        return (1,1)
    if a == 0:
        if b == 1 and c == 1:
            return (0,1)
        else:
            return (1,0)
    else:
        if b == 0 and c == 0:
            return (1,0)
        else:
            return (0,1)

def flip_array(A):
    i = 0
    j = len(A) - 1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

def binary_sum(A,B):
    # input: A and B are arrays of binary digits
    # output: array of binary digits
    c = 0
    i = len(A) - 1 
    j = len(B) - 1
    S = []
    while j >= 0 or i >= 0 or c == 1:
        if i < 0:
            a = 0
        else:
            a = A[i]
        if j < 0:
            b = 0
        else:
            b = B[j]
        s, c = full_adder(a,b,c)
        S.append(s)
        i -= 1
        j -= 1
    flip_array(S)
    return S