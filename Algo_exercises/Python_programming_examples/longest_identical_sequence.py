def longest_indentical_sequence(A):
    count = 1
    max_count = 1
    if len(A) == 0:
        max_count = 0
    else:
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
        
    print(max_count)

# ex 1
longest_indentical_sequence([8, -2, 3, 3, 4, 4, 4, 2, 2, 2, 3, -2, 3, 3, 3, 3, 4, 4, 4, 8, 2, 2, 8, 2, 2, 22, 2, 22, 22, 2, 2, 22, 8])

longest_indentical_sequence([])

longest_indentical_sequence([2, 2])