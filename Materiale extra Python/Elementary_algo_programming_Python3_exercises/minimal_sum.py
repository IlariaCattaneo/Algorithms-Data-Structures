def minimal_sum(A, x):
    s = 0
    for a in A:
        if a >= x:
            return True
        if a > 0:
            s = s + a
            if s >= x:
                return True
    return False