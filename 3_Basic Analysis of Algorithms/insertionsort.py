#1. Passing arguments to functions
def f(n):
    n = n + 1
    m = n + 2
    return n + m

def f(A):
    if len(A) > 1:
        A[1] = 0
    return 7

def g(n):
    n = n + 1
    return n

#2. Insertion sort
def insertion_sort(A):
    #changes A "in-place" so that A at the end contains every and all
    # the elements of A at the beginning, reordered in non-decreasing
    # order
    for i in range(1, len(A)):
        j = i
        while A[j] < A[j-1] and j > 0:
            #swap A[j] <==> A[j-1]
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
#memorize this algorithm!!!!        

import random
def random_array(n):
    A = []
    for _ in range(n):
        A.append(random.randint(1, 2*n))
    return A

def sorted_array(n):
    A = []
    for i in range(n):
        A.append(i)
    return A

def reversed_sorted_array(n):
    A = []
    for i in range(n-1):
        A.append(i)
    return A
