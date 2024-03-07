def mountain_sort(A):
    max = A[0]
    ind = 0
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
            ind = i
    A[len(A)//2], A[ind] = A[ind], A[len(A)//2]
    for i in range(len(A)//2):
        for j in range(i+1, len(A)//2):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]
    for p in range(len(A)//2, len(A)):
        for q in range(p+1, len(A)):
            if A[q] > A[p]:
                A[p], A[q] = A[q], A[p]
    return A

# This algorithm finds the maximum value of the array and puts it in the middle.
# Then it sorts the left part in the increasing order, by using 2 pointers and decreasing the length of the part.
# it does the same thing for the right part, which is sorted in decreasing order.
# This has complexity theta(nlogn)