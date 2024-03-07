def binary_search(A, x):
    # we assert that A is sorted in non-decreasing order
    # worst case complexity: theta(log n) -> there is no element
    # best case complexity: theta(1) -> we get at first time
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