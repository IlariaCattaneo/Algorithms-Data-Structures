def sum_of_three(A,s):
    i = 0
    B = merge_sort(A)
    for i in range(len(A)):
        j = 0
        k = len(A)-1
        while j < k:
            if j == i:
                j += 1
            elif k == i:
                k -= 1
            elif B[i] + B[j] + B[k] == s:
                return True
            elif B[i] + B[j] + B[k] > s:
                k -= 1
            else:
                j += 1
    return False

def merge_sort(A):
    if len(A) == 1:
        return A
    mid = len(A)//2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(A,B):
    i,j = 0,0
    X = []
    while i <= len(A) and j <= len(B):
        if i <= len(A) and (j > len(B) or A[i] < B[j]):
            X.append(A[i])
            i += 1
        else:
            X.append(B[j])
            j += 1
    return X