def count_lower(A,x):
    counter = 0
    for i in range(len(A)):
        if A[i] < x:
            counter += 1
    return counter

def leap_year(y):
    if y % 4 == 0 and (y % 400 == 0 or not y % 100 == 0):
        return True
    else:
        return False
    
def multiples_of_three(A):
    counter = 0
    for number in A:
        if number == 0:
            break
        if number % 3 == 0:
            counter += 1
    return counter

def check_sorted(A):
    if len(A) == 1 or len(A) == 0:
        return True
    else:
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return False
        return True
    
def find_peak(A):
    x = A[0]
    for number in A:
        if number > x:
            x = number
    return x

def partition_even_odd(A):
    pointer = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[pointer], A[i] = A[i], A[pointer]
            pointer += 1
    return A