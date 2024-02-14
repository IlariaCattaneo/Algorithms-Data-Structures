# exercise 1.1
def peak_element(A):
    for i in range(1,len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            print(i)

# exercise 1.2
# the function peak_element(A) returns the index of the peak element and has complexity O(n); 
# with this code we assume that the peak element cannot be the first or the last element of the array, 
# because we can't check if it's really a peak as before or after itself it doesn't have any number; 
# so we make the index start from position 1 and end in position len(A)-1

def logn_peak_element(A):
    max = 0
    Aleft = range(0,len(A)//2)
    Aright = range(len(A)//2,len(A))
    a = 0
    if Aleft[a] > max:
        max = a
        print(max)
        a += 1
    if Aright[a] > max:
        max = a
        print(max)
        a += 1
    logn_peak_element(Aleft)
    logn_peak_element(Aright)

# exercise 2.1
def count_battleship(B):
    count = 0
    for m,n in range(len(B)):
        if B[m][n] == 'X' and (B[m+1][n] == '0' and B[m][n+1] == '0'):
            count += 1
        if B[m][n] == 'X' and ((B[m+1][n] == '0' and B[m][n+1] == 'X') or (B[m+1][n] == 'X' and B[m][n+1] == '0')):
            count += 1
    return count

# exercise 2.2
# the worst case complexity is O(n^2) because we have to check every element of the matrix
# the best case complexity is O(n) because we have to check only the first element of the matrix
# the complexity in terms of m and n is O(m*n)

# exercise 3
def algo_x(A,B):
    C = [False] * len(A)
    for j in range(len(B)):
        i = 0
        while i <= len(A) and (C[i] == True or A[i] != B[j]):
            i += 1
        if i <= len(A):
            C[i] = True
        else:
            return False
    for i in range(len(A)):
        if C[i] == False:
            return False
    return True

# exercise 3.1
# the function algo_x(A,B) returns True if there are common elements in both A and B and False otherwise
# the function has complexity O(n^2)
# the worst case the complexity is O(n^2) because we execute the while loop
# the best case the complexity is O(n) because don't enter in the while loop

# exercise 3.2
def better_algo_x(A,B):
    C = [False] * len(A)
    for j in range(len(B)) and i in range(len(A)):
        if i <= len(A) and (C[i] == True or A[i] != B[j]):
            i += 1
        elif i <= len(A):
            C[i] = True
        else:
            return False
    for i in range(len(A)):
        if C[i] == False:
            return False
    return True

# exercise 4
def find_min_rectangle(points):
    maxd = 0
    for i in range(len(points)):
        for j in range(1, len(points)):
            # if points has a length less than 3, it's impossible to find a rectangle, so we return 0
            if len(points) <= 3:
                return 0
            # if 2 points have the same x coordinate, the height is the distance between their y coordinates
            if points[i][0] == points[j][0]:
                height = abs(points[i][1] - points[j][1])
            # if 2 points have the same y coordinate, the base is the distance between their x coordinates
            if points[i][1] == points[j][1]:
                base = abs(points[i][0] - points[j][0])
    return base * height