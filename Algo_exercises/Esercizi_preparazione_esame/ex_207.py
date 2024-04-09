def algo_s(A,k):
    for i in range(len(A)):
        if algo_r(A,A[i]) == k:
            return A[i]
    return None

def algo_r(A,y):
    c = 0
    for i in range(len(A)):
        if A[i] < y:
            c = c + 1
    return c

# algo s checks if there is an element that has k smaller numbers and returns that element
# wcc is theta(n^2) because we go through the nested loops to find the value; the worst case happens when we through the nested loops and we don't find the element so we return false

def better_algo_s(A,k):
    B = merge_sort(A)
    if k >= 0 and k < len(B) and B[k+1] > B[k]:
        return B[k+1]
    else:
        return None 
# wcc is theta(nlogn) given by the predomincance of the merge_sort algorithm

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