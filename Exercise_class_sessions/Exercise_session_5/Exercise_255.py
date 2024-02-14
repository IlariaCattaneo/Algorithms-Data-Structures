# linear complexity
def count_vertical(A):
    count = 0
    for xi in range(2,len(A),4):
        xp, yp = xi-2, xi-1
        yi = xi+1
        if (A[xp] == A[xi]): 
            count += 1
    return count

# linear complexity
def count_horizontal(A):
    count = 0
    for xi in range(2,len(A,),4):
        xp, yp = xi-2, xi-1
        yi = xi+1
        if (A[yp] == A[yi]): 
            count += 1
    return count

# def intersection(A):
#     for x1 in range(2,len(A)-4,4):
#         x0, y0 = x1-2, x1-1
#         y1 = x1+1
#         x2, y2 = x1+2, y1+2
#         x3, y3 = x1+4, y1+4

#         if (count_horizontal(A[x0:y1+1]) == 1 and count_vertical(A[x2:y3+1]) == 1):
#             if (A[x2] >= A[x0] and A[x2] <= A[x1] and A[y0] >= A[y2] and A[y0] <= A[y3]):
#                 return True
#         elif (count_vertical(A[x0:y1+1]) == 1 and count_horizontal(A[x2:y3+1]) == 1):
#             if (A[x0] >= A[x2] and A[x0] <= A[x3] and A[y2] >= A[y0] and A[y2] <= A[y1]):
#                 return True
#     return False

def intersection(A):
    for x1 in range(2,len(A),4):
        x0, y0 = x1-2, x1-1
        y1 = x1+1
        direction = -1            #0: horizontal, 1: vertical
        if (count_horizontal(A[x0:y1+1]) == 1): 
            direction = 0
        elif (count_vertical(A[x0:y1+1]) == 1):
            direction = 1
        else:
            continue
        
        for x3 in range(2,len(A),4):
            x2, y2 = x3-2, x3-1
            y3 = x3+1
            if (direction == 0 and count_vertical(A[x2:y3+1])):
                if (A[x2] >= A[x0] and A[x2] <= A[x1] and A[y0] >= A[y2] and A[y0] <= A[y3]):
                    return True
            elif (direction == 1 and count_horizontal( A[x2:y3+1])):
                if (A[x0] >= A[x2] and A[x0] <= A[x3] and A[y2] >= A[y0] and A[y2] <= A[y1]):
                    return True

    return False