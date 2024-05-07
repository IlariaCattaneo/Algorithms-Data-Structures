def maximal_step_k_length(A,k):
    max_length = 0
    current_length = 0
    for i in range(len(A)-1):
        if abs(A[i] - A[i+1]) == k:
            current_length += 1
        else:
            if max_length < current_length:
                max_length = current_length
            current_length = 0
    if max_length < current_length:
        max_length = current_length
    return max_length