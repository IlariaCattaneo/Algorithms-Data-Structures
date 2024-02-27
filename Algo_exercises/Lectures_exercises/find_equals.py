def find_equals(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return True
    return False

# best case complexity -> when we find the two numbers at the beginning of the array -> theta(1)
# worst case complexity -> we need to scan the entire array n-1 every time and we don't find the pair of equal numbers n(n+1)/2 ->theta(n^2)