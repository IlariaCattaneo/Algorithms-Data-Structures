def count_lower(A,x):
    counter = 0
    for i in range(0, len(A), 1):
        if A[i] < x:
            counter += 1
    print(counter)
        