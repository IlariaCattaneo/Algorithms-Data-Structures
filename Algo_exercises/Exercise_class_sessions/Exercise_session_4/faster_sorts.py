def bubble_sort( A ):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if( A[i] > A[j]):
                A[i], A[j] = A[j], A[i]
    return A

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    return A

def selection_sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A)//2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)