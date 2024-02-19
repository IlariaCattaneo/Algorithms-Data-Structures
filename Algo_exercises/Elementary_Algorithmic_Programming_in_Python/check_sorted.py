def check_sorted(A):
    if len(A) == 1 or len(A) == 0:
        return True
    else:
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                return False
        return True

# Ex 1
print(check_sorted([1,2,3]))

# Ex 2
print(check_sorted([1,3,2]))

# Ex 3
print(check_sorted([]))

# Ex 4
print(check_sorted([7]))

# Ex 5
print(check_sorted([50,50,50]))

# Ex 6
print(check_sorted([43,51,51]))

# Ex 7
print(check_sorted([43,51,50,51,70]))
