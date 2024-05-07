def lower_bound(A,x):
    # A is already sorted
    if x > len(A):
        return "Error: not found"
    l = 0
    h = len(A) - 1
    while l < h:
        mid = (l+h)//2
        if A[mid] < x:
            l = mid + 1
        else:
            h = mid
    return A[h]
    
