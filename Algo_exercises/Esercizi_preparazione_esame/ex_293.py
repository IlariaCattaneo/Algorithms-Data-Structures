def algo_x(A,B):
    V = []
    for i in range(len(B)):
        V.append(0)
    for i in range(len(A)):
        x = False
        j = 0
        while j <= len(B) and x == False:
            if A[i] == B[j] and V[j] == 0:
                x = True
                V[j] = 1
            else:
                j += 1
    for j in range(len(B)):
        if V[j] == 0:
            return False
    return True

# algo_x returns true if and only if the elements of B are a subset of the elements of A
# worst-case complexity: theta(n^2) because we have to execute the nested loops; happens when we iterate and we don't find any element of A in B
# best-case complexity: theta(n^2)

def better_algo_x(A,B):
    C = A.sort()
    D = B.sort()
    j,i = 0,0
    while j <= len(D) and i <= len(C):
        if D[j] == C[i]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(D) - 1:
        return True
    else:
        return False
