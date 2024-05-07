def high_power_sum(A,h,t):
    count_variations = 0
    count_time = 1
    max_var = 0
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            count_variations += (A[i+1] - A[i])
            count_time += 1
            if count_variations > max_var and count_time <= t:
                max_var = count_variations
                min_time = count_time
        else:
            count_time = 1
            count_variations = 0
    if max_var >= h and min_time <= t:
        return True
    else:
        return False