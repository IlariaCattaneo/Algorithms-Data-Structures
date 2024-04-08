# ex 206
def algo_x_206(A,x):
    i = len(A) - 1
    j = 0
    while i >= 0:
        if j == i:
            j = 0
            i = i - 1
        elif A[i] - A[j] > x or A[j] - A[i] > x:
            return True
        else:
            j = j + 1
    return False
# algo x checks if there are any pair of numbers whose difference is greater than x
# worst case complexity is theta(n^2) because we scan everything twice everytime to find the pair of numbers; wcc happens especially when the algorithm doesn't find a pair of numbers and returns false

def better_algo_x_206(A,x):
    if len(A) < 2:
        return False
    max = A[0]
    min = A[0]
    for num in A:
        if num < min:
            min = num
        elif num > max:
            max = num
    return max - min > x


# ex 253
def algo_x_253(A,k):
    B = algo_y_253(A,0,len(A))
    c = 0
    for i in range(len(B)):
        if i < k:
            c = c + B[i]
        else:
            return c
    return c

def algo_y_253(A,i,j):
    D = []
    if j - i == 1:
        D.append(A[i])
    elif j - i > 1:
        k = (i + j)//2
        B = algo_y_253(A,i,k)
        C = algo_y_253(A,k,j)
        b = 0
        c = 0
        while b < k - i or c < j - k:
            if c >= j - k or (b < k - i and B[b] < C[c]):
                D.append(B[b])
                b = b + 1
            else:
                D.append(C[c])
                c = c + 1
    return D
# algo y is the reproduction of a merge-sort
# algo x returns the sum of numbers until the k-th position, which means the sum of numbers in the first k positions
# worst case complexity is theta(nlogn); algo y is theta(nlogn) which is the complexity of merge-sort and in algo x we scan array B in theta(n), so combining them we take the highest order which is theta(nlogn)
# wcc happens mainly when we do the sorting, which happens quite always
# also best case complexity is theta(nlogn) best the predomincance is given by the merge-sort

def sum_253(A):
    sum = 0
    for i in range(len(A)):
        s += A[i]
    return sum

import random
def better_algo_x_253(A,k):
    if k >= len(A):
        return sum_253(A)
    v = random.choice(A)
    L, M, R = [], [], []
    i = 0
    for i in range(len(A)):
        if A[i] < v:
            L.append(A[i])
        elif A[i] > v:
            R.append(A[i])
        else:
            M.append(A[i])
    if k < len(L):
        return better_algo_x_253(L,k)
    if k - len(L) <= len(M):
        return sum_253(L) + (k-len(L))*v
    return sum_253(L) + sum_253(M) + better_algo_x_253(R,k-len(L)-len(M))
# this algo uses the k-selection which is a divide and conquer algorithm
# it works in theta(n^2) in worst case but in theta(n) in both average and best case


# ex 254
def algo_x_254(A,x):
    for i in range(len(A)):
        if algo_y_254(A,i,len(A),A[i]+x):
            return True
    return False

def algo_y_254(A,i,j,x):
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

def better_algo_x_254(A,x):
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


# ex 288
def algo_y_288(T):
    x = 0
    for i in range(len(T)):
        l = T[i].amount
        r = T[i].amount
        for j in range(len(T)):
            if i != j:
                if T[j].date <= T[i].date and T[i].date - T[j].date <= 10:
                    l = l + T[j].amount
                if T[j].date >= T[i].date and T[j].date - T[i].date <= 10:
                    r = r + T[j].amount
        if x < r:
            x = r
        if x < l:
            x = l
    return x
# algo y returns the highest sum of distinct sales transactions that have a time distance of less than 10 days
# worst case complexity is theta(n^2), because we always compute the nested loops; therefore also best case complexity is theta(n^2)

def better_algo_y_288(T):
    S = sorted(T) # sorted copy of T by date
    i,j = 0,0
    sum_of_trans,max_trans = 0,0
    while j <= len(S):
        if S[j].date - S[i].date <= 10:
            sum_of_trans += S[j].amount
            j += 1
            if sum_of_trans > max_trans:
                max_trans = sum_of_trans
        else:
            sum_of_trans -= S[i].amount
            i += 1
    return max_trans
# we sort T in theta(nlogn) and then we do a linear scan of the sorted array in theta(n)
# overall complexity is theta(nlogn)