def find_peak(A):
    x = A[0]
    for number in A:
        if number > x:
            x = number
    return x

def find_peak_binarysearch(A):
    begin = 0
    end = len(A)
    if len(A) == 0:
        return None
    elif len(A) == 1:
        return A[0]
    while begin < end:
        mid = (begin + end)//2
        if abs(begin-(end-1)) == 1 or abs(begin-(end-1)) == 0:
            if A[begin] > A[end-1]:
                return A[begin]
            else:
                return A[end-1]
        elif (A[mid - 1] <= A[mid] and A[mid] >= A[mid + 1]):
            return A[mid]
        elif A[mid] >= A[mid - 1]:
            begin = mid + 1
        elif A[mid] <= A[mid - 1]:
            end = mid
    return A[begin]
