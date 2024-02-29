def partition_even_odd_1(A):
    pointer = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[pointer], A[i] = A[i], A[pointer]
            pointer += 1
    print(A)
        
def partition_even_odd_2(A):
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 == 0:
            i += 1
        elif A[j] % 2 != 0:
            j -= 1
        else:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    print(A)

# ex 1
partition_even_odd_1([-1, 1, 7, 5, -2, 1, 2, 7, 7, 5, 5, 1, 1, 4, 1])