def algo_x(A):
    i = 1 
    j = len(A) + 1
    while i < j:
        if A[i] % 2 == 0:
            j -= 1 
            v = A[i]
            algo_y(A, i, j)
            A[j] = v
        else:
            i += 1
    return j

def algo_y(A, p, q):
    while p < q:
        A[p] = A[p+1]
        p = p + 1

# shifta gli elementi a sinistra, 
# spostando i numeri pari alla fine dell'array 
# ritorna l'indice al quale partono i numeri pari

def better_algo_x(A):
    i = 0
    j = len(A)
    while i < j:
        if A[i] % 2 == 0:
            j -= 1
            tmp = A[i]
            A[i] = A[i+1]
            i += 1
            A[j] = tmp
        else: 
            i += 1
    return j
