def partition_even_odd(A):
    pointer = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[pointer], A[i] = A[i], A[pointer]
            pointer += 1
    print(A)
        
# ex 1
partition_even_odd([-1, 1, 7, 5, -2, 1, 2, 7, 7, 5, 5, 1, 1, 4, 1])