def algo_x(A,B):
    for l in range(len(A),0):
        for j in range(len(B)):
            for i in range(len(A)-l+1):
                s = 0
                for k in range(i,i+l-1):
                    s += A[k]
                if s == B[j]:
                    return l
    return 0

# Algo-X returns the maximal length of any contiguous subsequence of A whose total value is equal to an element of B. If no such sequence exists, the result is 0.
# worst-case: when the result is 0, which happens when the algorithm iterates through its four nested loops. complexity O(n4).

def algo_x(A,B):
    for l in range(len(A),0):
        for j in range(len(B)):
            s = 0
            for k in range(l):
                s += A[k]
            if s == B[j]:
                return l
            for i in range(3,len(A)-l+1):
                s -= (A[i] + A[i+l-1])
                if s == B[j]:
                    return l
    return 0