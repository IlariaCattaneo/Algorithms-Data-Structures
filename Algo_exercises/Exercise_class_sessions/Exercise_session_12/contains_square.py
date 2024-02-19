A = [
[7, 8, 3, 8, 8, 3],
[7, 8, 3, 3, 3, 3],
[1, 3, 3, 5, 8, 3],
[7, 6, 3, 5, 3, 3],
[0, 4, 3, 3, 3, 3],
[9, 9, 1, 3, 7, 3]
]

def contains_square(A):
    for i in range(len(A)-1):
        for j in range(len(A[i])-1):
            if A[i][j] == A[i][j+1] == A[i+1][j] == A[i+1][j+1]:
                return True