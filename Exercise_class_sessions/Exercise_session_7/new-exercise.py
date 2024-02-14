def algo_x(A):
    s = 0
    n = 0
    for i in range(1, len(A)):
        s = s + A[i]
        n += 1
        return algo_y(A, s, n)
    
def algo_y(A, p, q):
    m = p / q
    s = 0
    for j in range(1, len(A)):
        if A[j] < m:
            s += 1
    return s

# Algo-x computa la media e ritorna quanti numeri sono minori della media 