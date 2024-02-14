def merge(A, B):
    # we assert/assume that A and B are both sorted
    X = [] # this is the output array, in which A and B are merged
    i = 0 # index in A
    j = 0 # index in B
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            X.append(A[i])
            i = i + 1
        else: 
            X.append(B[j])
            j = j + 1
    while i < len(A):
        X.append(A[i])
        i = i + 1 
    while j < len(B):    
        X.append(B[j])
        j = j + 1 
    return X

def better_merge(A, B):
    # we assert/assume that A and B are both sorted
    X = [] # this is the output array, in which A and B are merged
    i = 0 # index in A
    j = 0 # index in B
    while i < len(A) or j < len(B):
        if j == len(B) or (i < len(A) and A[i] <= B[j]):
            X.append(A[i])
            i = i + 1
        else: 
            X.append(B[j])
            j = j + 1
    return X

def better_merge_sort(A, begin, end):
    if (end - begin) < 2:
        return A[begin:end]
    m = (end + begin) // 2
    L = better_merge_sort(A, begin, m)
    print(L)
    R = better_merge_sort(A, m, end)
    print(R)
    return better_merge(L, R)

def merge_sort(A):
    if len(A) < 2:
        return A
    m = len(A) // 2
    L = merge_sort(A[:m])
    R = merge_sort(A[m:])
    return better_merge(L, R)