def find(A,x):
    for i in A:
        if i == x:
            return True
    return False

# best case complexity -> when x is found in the first position of the array -> O(1), theta(1)
# worst case complexity -> when we scan all the array and we don't find x -> theta(n)
# average case complexity -> when we scan the array and x is in the middle -> theta(n)
