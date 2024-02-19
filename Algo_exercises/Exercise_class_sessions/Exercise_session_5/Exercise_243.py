def rotate(A,k):
    A = A[k:len(A)] + A[0:k]
    return A

def rotate_in_place(A,k):
    for count in range(0,k):
        i = A[0]
        A.remove(A[0])
        A.append(i)
    return A
# this algo is in place but it's not good, because remove has complexity Theta(n) 
# so the algo has complexity O(n^2)

def right_rotate_in_place(A, k):
    n = len(A)
    k = k % n
    if k == 0:
        return
    cycle_start = 0
    v = A[cycle_start]
    i = 0
    for _ in range(n):
        i = (i + k) % n
        A[i], v = v, A[i]
        if i == cycle_start:
            cycle_start += 1
            v = A[cycle_start]
            i = cycle_start
