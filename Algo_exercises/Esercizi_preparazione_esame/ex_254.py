def algo_x(A,x):
    for i in range(len(A)):
        if algo_y(A,i,len(A),A[i]+x):
            return True
    return False

def algo_y(A,i,j,x):
    while j > i:
        k = (i + j)//2
        if x < A[k]:
            j = k
        elif x > A[k]:
            i = k + 1
        else:
            return True
    return False
# algo x checks whether there exists a pair of numbers whose distance is equal to x
# worst case complexity is theta(nlogn), which corresponds to an input array that contains no elements at distance x
# best case complexity is O(1), constant in the case in which the first element is y and there is an element that corresponds to y + x

def better_algo_x(A,x):
    i = 0
    j = 1
    while j < len(A):
        if A[j] < A[i] + x:
            j += 1
        elif A[j] > A[i] + x:
            i += 1
        else:
            return True
    return False