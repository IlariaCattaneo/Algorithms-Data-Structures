def duplicates(A):
    j = 0
    while j < len(A)-1:
        if A[j] == A[j+1]:
            A.pop(j+1)
        else:
            j += 1
    return A

def stops_and_inversions(P):
    A = []
    stops = 0
    inversions = 0
    for i in range(len(P)-1):
        if i == len(P)-1 and P[i] == P[i-1]:
            A.append('stopped')
        elif i == len(P)-1 and P[i] > P[i-1]:
            A.append('ascending')
        elif i == len(P)-1 and P[i] < P[i-1]:
            A.append('descending')
        elif i < len(P)-1 and P[i] == P[i+1]:
            A.append('stopped')
        elif i < len(P)-1 and P[i] > P[i+1]:
            A.append('descending')
        elif i < len(P)-1 and P[i] < P[i+1]:
            A.append('ascending')
    print(A)
    duplicates(A)
    print(A)
    for k in range(1, len(A)-1):
        if A[k] == 'stopped':
            stops += 1
        if k+1 == len(A)-1 and A[k+1] == 'stopped':
            stops += 1
        elif k == 1 and A[k-1] == 'stopped':
            stops += 1
        if (A[k-1] == 'ascending' and A[k] == 'stopped' and A[k+1] == 'descending') or (A[k-1] == 'descending' and A[k] == 'stopped' and A[k+1] == 'ascending'):
            inversions += 1
        elif (A[k-1] == 'ascending' and A[k] == 'descending') or (A[k-1] == 'descending' and A[k] == 'ascending'):
            inversions += 1
    print('Stops:', stops)
    print('Inversions:', inversions)

# ex 1
stops_and_inversions([])

# ex 2
stops_and_inversions([5,5,5])

# ex 3
stops_and_inversions([5,5,5,6,7,8])

# ex 4
stops_and_inversions([5,5,5,6,7,8,8])

# ex 5
stops_and_inversions([1,5,10,12,12,12,15,20,24])

# ex 6
stops_and_inversions([1,5,10,12,12,11,8,7])

# ex 7
stops_and_inversions([1,5,10,12,12,11,8,7,9,11,20,30])