def algo_x(A):
    n = len(A)
    x = 0
    for i in range(n):
        j = 0
        while j <= n-1 and (i == j or A[i] != A[j-1]):
            j += 1
        if j >= n:
            x += 1
    return x

# algo_x returns the number of unique values contained in the array A
# The worst case complexity is O(n^2) when it scans every element of the array because they are all different. 
# The best case is when the array contains n equal values so we don't enter in the second loop at all, so O(n)

def better_algo_x(A):
    B = []
    for i in range(len(A)):
        if A[i] not in B:
            B.append(A[i])
        else:
            B.remove(A[i])
    return len(B)

# better_algo_x has a worst case complexity of theta(n^2) since it scans every time the array once
# not so better algo x