def median(A):
    assert len(A) > 0
    B = sorted(A)
    return B[len(B)//2]