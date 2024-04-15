def algo_x(A,B):
    C = B.copy()
    n = len(C)
    for i in range(len(A)):
        j = 0
        while j <= n:
            if A[i] == C[j]:
                C[j],C[n] = C[n],C[j]
                n -= 1
            else:
                j += 1
    if n == 0:
        return True
    else:
        return False
# algo_x checks if array B/C contains a subset of numbers of A
# wcc: theta(n^2) because we need to execute the outer and inner loops everytime, happens when we need to scan and no element of A is found returning false

def better_algo_x(A,B):
    C = heap_sort(A)
    D = heap_sort(B)
    n = len(D)
    i,j = 0,0
    while i <= len(C) and j <= len(D):
        if C[i] < D[j]:
            i += 1
        elif C[i] > D[j]:
            j += 1
        else:
            n -= 1
            i += 1
            j += 1
    if n == 0:
        return True
    else:
        return False
    
def heap_sort(A):
    heap_size = len(A)
    build_max_heap(A)
    for i in range(len(A),0):
        A[1], A[i] = A[i], A[1]
        heap_size -= 1
        max_heapify(A,1)

def build_max_heap(A):
    heap_size = len(A)
    for i in range(heap_size//2,0):
        max_heapify(A,i)

def max_heapify(A,i):
    l = 2*i
    r = 2*i + 1
    heap_size = len(A)
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A,largest)
