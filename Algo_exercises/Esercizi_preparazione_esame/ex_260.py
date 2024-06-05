def longest_mirror_seq(A,B):
    n = len(A)
    max = 0
    for i in range(len(A)):
        for j in range(len(B)):
            l = 0
            while i+l < n and j-l >= 0 and A[i+l] == B[j-l]:
                l += 1
            if l > max: 
                max = l
    return max

def better_longest_mirror_seq(A,B):
    m = 0
    for p in range(1,len(A)+1):
        l = 0
        i = 0
        while i < p and i < len(B):
            if A[p-i-1] == B[i]:
                l += 1
                if l > m:
                    m = l
            else:
                l = 0
            i += 1
    for p in range(1,len(B)):
        l = 0
        i = p
        while i < len(B) and len(A)-1-i+p >= 0:
            if A[len(A)-1-i+p] == B[i]:
                l += 1
                if l > m:
                    m = l
            else:
                l = 0
            i += 1
    return m