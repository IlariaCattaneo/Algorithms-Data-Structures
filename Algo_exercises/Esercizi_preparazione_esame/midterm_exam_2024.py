# EXERCISE 2
def algo_x(A):
    n = len(A)
    x = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[k] - A[j] == 1 and A[j] - A[i] == 1:
                    x += 1
    return x

# explain what the function algo_x does and its complexity

# Algo_x counts the number of triplets (that have distance 1 between one number and the adjacent one) 
# that are in decreasing order that appear in the array A
# So if we have an array A=[4,7,3,1,0,2] we should have 3 triplets that satisfy the condition: 4,3,2 and 3,2,1 and 2,1,0 and x should be equal to 3

# Worst case complexity is theta(n^3) since to search for the triplets we execute all nested loops. 
# It happens especially when we scan the entire array and we don't find a triplet and so we return 0

# Best case complexity is still theta(n^3) because we search for any triplet amd therefore we execute all the nested loops

# write a better_algo_x(A) with strictly better complexity than algo_x
def better_algo_x(A):
    count = 0
    A = heap_sort(A)
    for i in range(len(A)-2):
        if A[i+1] - A[i] == 1 and A[i+2] - A[i+1] == 1:
            count += 1
    return count

# Worst case complexity is theta(nlogn) and best case complexity is theta(nlogn). 
# In both cases heap_srt predominates the complexity since it is theta(nlogn)

def heap_sort(A):
    heap_size = len(A)
    build_min_heap(A)
    for i in range(len(A),0):
        A[1], A[i] = A[i], A[1]
        heap_size -= 1
        min_heapify(A,1)

def build_min_heap(A):
    heap_size = len(A)
    for i in range(heap_size//2,0):
        min_heapify(A,i)

def min_heapify(A,i):
    l = 2*i
    r = 2*i + 1
    heap_size = len(A)
    if l <= heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        min_heapify(A,smallest)

# EXERCISE 3
def algo_dna(X,Y):
    X = merge_sort(X)
    Y = merge_sort(Y)
    j = 0
    for i in range(len(X)):
        if j > len(Y):
            return True
        if X[i] > Y[j]:
            return False
        if X[i] == Y[j]:
            j += 1
    if j > len(Y):
        return True
    else:
        return False
    
def merge_sort(A):
    if len(A) < 2:
        return A
    m = len(A) // 2
    L = merge_sort(A[:m])
    R = merge_sort(A[m:])
    return better_merge(L, R)

def better_merge(A, B):
    # we assert/assume that A and B are both sorted
    X = [] # this is the output array, in which A and B are merged
    i = 0 # index in A
    j = 0 # index in B
    while i < len(A) or j < len(B):
        if j == len(B) or (i < len(A) and A[i] <= B[j]):
            X.append(A[i])
            i = i + 1
        else: 
            X.append(B[j])
            j = j + 1
    return X

# Algo_dna checks if the two dna sequences X and Y are almost the same (Y<=X).
# Worst case complexity is theta(nlogn) given by the predominance of the merge_sort over the for-loop (which theta(n))
# Best case complexity is still theta(nlogn) for the same reason. We always execute the merge_sort

def better_algo_dna(X,Y):
    ax,ay,cx,cy,gx,gy,tx,ty = 0,0,0,0,0,0,0,0
    for i in range(len(X)):
        if X[i] == 'A':
            ax += 1
        elif X[i] == 'C':
            cx += 1
        elif X[i] == 'G':
            gx += 1
        elif X[i] == 'T':
            tx += 1
    for i in range(len(Y)):
        if Y[i] == 'A':
            ay += 1
        elif Y[i] == 'C':
            cy += 1
        elif Y[i] == 'G':
            gy += 1
        elif Y[i] == 'T':
            ty += 1
    if ax != ay:
        return False
    if ax >= ay:
        if cx >= cy and gx >= gy and tx >= ty:
            return True
    return False

# Worst case complexity is theta(n) given by the for-loop that scans the two sequences
# Best case complexity is theta(n) for the same reason. We always scan the two sequences

# EXERCISE 4
# write an algo valid_range(A,t,k) that returns the average of all the valid measurements in A, or an error if there are no valid measurements.
def valid_average(A,T,k):
    positive = []
    valid = []
    for i in range(len(A)):
        if A[i] > 0:
            positive.append(A[i])
    sum = 0
    if len(positive) == 0:
        return "error"
    elif len(positive) <= k:
        for i in range(len(positive)):
            sum += A[i]
        return sum/len(positive)
    else:
        for i in range(len(positive)):
            if i < k:
                valid.append(positive[i])
            elif positive[i]-sum(valid[i-k:i])/k <= T:
                valid.append(positive[i])
        sum_valid = 0
        for i in range(len(valid),len(valid)-k):
            sum_valid += valid[i]
        return sum_valid/k
