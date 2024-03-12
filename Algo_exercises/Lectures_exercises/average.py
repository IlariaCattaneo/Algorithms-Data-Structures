def average(A):
    assert len(A) > 0
    sum = 0
    for number in A:
        sum += number 
    return sum/len(A)