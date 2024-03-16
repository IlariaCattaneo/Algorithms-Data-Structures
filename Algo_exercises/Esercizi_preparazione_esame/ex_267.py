def algo_y(A, r, c):
    for i in range(r*c):
        for j in range(i+1, r*c):
            if A[i] != A[j]:
                a = (i-1)//c
                b = (j-1)//c
                if a == b or a == b-1:
                    if i - a*c == j - b*c or i - a*c == j - b*c + 1 or i - a*c == j - b*c -1:
                        return True
    return False

# algo y checks whether any two adjacent positions in the matrix contain equal elements.
# worst case complexity is when there are no equal numbers and the loops go through the matrix either way -> theta(n^2)
# best case complixity is when the first element has an equal adjacent element -> O(1)

def better_algo_y(A, r, c):
    assert r == len(A) and r == c
    # check angles
    if A[0][0] == A[0][1] or A[0][0] == A[1][0]: # angolo in alto a sinistra
        return True
    if A[len(A)-1][0] == A[len(A)-1][1] or A[len(A)-1][0] == A[len(A)-2][0]: # angolo in basso a sinistra
        return True
    if A[0][len(A)-1] == A[0][len(A)-2] or A[0][len(A)-1] == A[1][len(A)-1]: # angolo in alto a destra
        return True
    if A[len(A)-1][len(A)-1] == A[len(A)-1][len(A)-2] or A[len(A)-1][len(A)-1] == A[len(A)-2][len(A)-1]: # angolo in basso a destra
        return True
    # check borders
    for i in range(1, len(A)-1):
        if A[0][i] == A[0][i-1] or A[0][i] == A[0][i+1] or A[0][i] == A[1][i]: # check top border
            return True
        if A[i][0] == A[i-1][0] or A[i][0] == A[i+1][0] or A[i][0] == A[i][1]: # check left
            return True
        if A[len(A)-1][i] == A[len(A)-1][i-1] or A[len(A)-1][i] == A[len(A)-1][i+1] or A[len(A)-1][i] == A[len(A)-2][i]: # check bottom
            return True
        if A[i][len(A)-1] == A[i-1][len(A)-1] or A[i][len(A)-1] == A[i+1][len(A)-1] or A[i][len(A)-1] == A[i][len(A)-2]: # check right
            return True
    # check center
    for row in range(1, len(A)-1):
        col = 1
        if A[row][col] == A[row][col-1] or A[row][col] == A[row][col+1] or A[row][col] == A[row-1][col] or A[row][col] == A[row+1][col]:
            return True
        else: 
            col += 1
            if A[row][col] == A[row][col-1] or A[row][col] == A[row][col+1] or A[row][col] == A[row-1][col] or A[row][col] == A[row+1][col]:
                return True
    # if no equal adjacent elements are found
    return False