def algo_x(A, x):
    for i in range(1, len(A)):
        if algo_y(A, i+1, len(A) + 1, A[i] + x):
            return True
    return False
    
def algo_y(A, i, j, x):
    while j > i:
        k = (i+j) // 2
        if x < A[k]:
            j = k 
        elif x > A[k]:
            i = k + 1 
        else: 
            return True
    return False

# the function algo_x(A, x) returns True if there are two elements in A that sum up to x, False otherwise.
# the worst case complexity of algo_x is O(n^2), because the function algo_y is called n times, and the worst case complexity of algo_y is O(n).
# the best case complexity of algo_x is O(n), because the function algo_y is called n times, and the best case complexity of algo_y is O(1).
# the average case complexity of algo_x is O(n^2), because the function algo_y is called n times, and the average case complexity of algo_y is O(n).

def better_algo_x(A, x):
    A.sort()
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == x:
            return True
        elif A[i] + A[j] < x:
            i += 1
        else:
            j -= 1
    return False
# the worst case complexity of better_algo_x is O(nlogn)
# the best case complexity of better_algo_x is O(nlogn)