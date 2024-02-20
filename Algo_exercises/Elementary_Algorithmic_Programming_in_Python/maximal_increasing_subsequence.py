def maximal_increasing_subsequence(A):
    counter = 1
    max = 0
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            counter += 1
        else:
            if counter > max:
                max = counter    
                counter = 1
    print(max)
    
# ex 1
maximal_increasing_subsequence([-1, 1, 7, 5, -2, 1, 2, 7, 7, 5, 0, 1, 3, 4, 1])