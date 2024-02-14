# We say that an array A is in "e-top" order when  A[i] ≤ A[j] for all i, j  such
# that i is odd and j is even. Write an algorithm  Sort-E-Top(A)  that sorts an array A in e-
# top order with an average-case time complexity of  O(n) . You may want to use standard,
# well-known algorithms. However, you must explicitly write their pseudo-code.

def Sort_E_Top(A):
    # Sort the odd elements in A
    A[1::2] = sorted(A[1::2])
    # Sort the even elements in A
    A[::2] = sorted(A[::2])
    return A
