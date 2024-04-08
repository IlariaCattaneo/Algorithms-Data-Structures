def algo_x(A,x):
    i = len(A) - 1
    j = 0
    while i >= 0:
        if j == i:
            j = 0
            i = i - 1
        elif A[i] - A[j] > x or A[j] - A[i] > x:
            return True
        else:
            j = j + 1
    return False
# algo x checks if there are any pair of numbers whose difference is greater than x
# worst case complexity is theta(n^2) because we scan everything twice everytime to find the pair of numbers; wcc happens especially when the algorithm doesn't find a pair of numbers and returns false

def better_algo_x(A,x):
    if len(A) < 2:
        return False
    max = A[0]
    min = A[0]
    for num in A:
        if num < min:
            min = num
        elif num > max:
            max = num
    return max - min > x