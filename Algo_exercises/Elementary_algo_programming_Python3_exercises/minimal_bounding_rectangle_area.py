# given 2 arrays of x and y coordinates, find the area of the smallest axis-aligned rectangle that contains all the points
# X and Y are 1D arrays of the same length
def minimal_bounding_rectangle_area(X,Y):
    i,j = 0,0
    maxx = X[0]
    minx = X[0]
    miny = Y[0]
    maxy = Y[0]
    while i < len(X) and j < len(Y):
        print(f'X[{i}] = {X[i]}', f'Y[{j}] = {Y[j]}', 
              f'maxx = {maxx}', f'minx = {minx}', f'maxy = {maxy}', 
              f'miny = {miny}')
        if X[i] > maxx:
            maxx = X[i]
        if X[i] < minx:
            minx = X[i]
        if Y[j] < miny:
            miny = Y[j]
        if Y[j] > maxy:
            maxy = Y[j]
        i += 1
        j += 1
    return (maxx - minx) * (maxy - miny)


