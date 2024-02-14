def binary_search(A, x):
    # complexity: theta(log n)
    begin = 0
    end = len(A)
    while begin < end:
        middle = (begin + end) // 2
        if x > A[middle]:
            begin = middle + 1
        elif x < A[middle]:
            end = middle
        else:
            return True
    return False