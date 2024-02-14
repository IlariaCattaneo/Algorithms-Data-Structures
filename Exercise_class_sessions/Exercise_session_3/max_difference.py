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

def maximal_difference(A):
    insertion_sort(A)
    maxd = A[len(A)-1] - A[0]
    return maxd