def algo_x(A):
    n = len(A)
    B = [None]*n
    for i in range(n):
        B[i] = 0
    m = 1
    x = A[1]
    for i in range(n):
        if B[i] == 0:
            B[i] = 1
            for j in range(i+1,n):
                if A[i] == A[j]:
                    B[i] += 1
                    B[j] = 1
                    if B[i] > m or (B[i] == m and A[i] < x):
                        m = B[i]
                        x = A[i]
    return x

# if they are all distinct numbers it returns the minimum number
# if there are some duplicates it returns the minimum number that has maximum number of duplicates
# theta(n^2)

def better_algo_x(A):
    n = len(A)
    B = {}
    max_rep = 1
    min_num = A[0]
    for i in range(n):
        # if A[i] is not a key of B, we add it to B
        if A[i] not in B:
            B[A[i]] = 1
        else:
            B[A[i]] += 1
            print(B)
            if B[A[i]] > max_rep or (B[A[i]] == max_rep and A[i] < min_num):
                max_rep = B[A[i]]
                min_num = A[i]
    return min_num