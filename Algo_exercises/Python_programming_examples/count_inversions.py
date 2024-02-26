def count_inversions(A):
    count = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if i < j and A[i] > A[j]:
                count += 1
    return count
    
print(count_inversions([9, 5, 3, 4, 6, 4, 5, 2, 43, 56]))

print(count_inversions([1, 2, 3, 4, 5, 5, 5, 5, 5, 6]))
