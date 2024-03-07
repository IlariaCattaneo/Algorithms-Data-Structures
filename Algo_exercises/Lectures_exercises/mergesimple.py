from binary_search import binary_search

def find_in_subsequence(A, begin, end, x):
    assert begin <= len(A) and end <= len(A)
    for i in range(begin, end):
        if A[i] == x:
            return True
    return False

def mergesimple(A, B):
    X = []
    for i in range(len(A)):
        if not find_in_subsequence(A, 0, i-1, A[i]):
            X.append(A[i])
    for i in range(len(B)):
        if not find_in_subsequence(A, B[i]) and not find_in_subsequence(B, 0, i-1, B[i]):
            X.append(B[i])
    return X

def mergesimple2(A, B):
    X = []
    for i in range(len(A)):
        if not binary_search(A, A[i]):
            X.append(A[i])
    for i in range(len(B)):
        if not binary_search(B, B[i]):
            X.append(B[i])
    return X