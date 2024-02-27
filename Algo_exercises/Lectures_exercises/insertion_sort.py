def insertion_sort(A):
    if len(A) < 2:
        return
    for i in range(1,len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1

# best case complexity -> array is already sorted -> theta(n)
# worst case complexity -> theta(n^2)