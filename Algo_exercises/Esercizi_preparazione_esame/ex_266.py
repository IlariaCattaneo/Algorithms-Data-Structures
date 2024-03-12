def algo_x(A):
    for i in range (len(A)):
        s = 0
        for j in range(len(A)):
            if i != j:
                s = s + A[j]
        if A[i] == s:
            return True
    return False

# algo x checks if A[i] is equal to the sum of all other elements in A
# worst case complexity happens when we scan the entire array for each element and we don't find any match -> theta(n^2)
# best case complexity we find the sum of the other elements in the first element of the array -> theta(n)

def better_algo_x(A):
    s = 0
    for i in range(len(A)):
        s += A[i]
    for j in range(len(A)):
        if A[j] == s - A[j]:
            return True
    return False