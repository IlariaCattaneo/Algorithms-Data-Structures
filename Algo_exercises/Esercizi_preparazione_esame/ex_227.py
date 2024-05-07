def questionable_sort(A):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
# questionable_sort is the selection_sort algorithm, it has a time complexity of theta(n^2) because it has to scan the array n times and for each scan it has to scan the remaining part of the array

def better_sort(A):
    heap_sort(A)

def heap_sort(A):
    build_max_heap(A)
    for i in range(len(A),0):
        A[1], A[i] = A[i], A[1]
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