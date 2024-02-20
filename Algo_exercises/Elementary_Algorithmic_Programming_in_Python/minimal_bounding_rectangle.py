def minimal_bounding_rectangle_area(X,Y):
    i,j = 0,0
    maxx = X[0]
    minx = X[0]
    miny = Y[0]
    maxy = Y[0]
    while i < len(X) and j < len(Y):
        # print(f'X[{i}] = {X[i]}', f'Y[{j}] = {Y[j]}', 
        #       f'maxx = {maxx}', f'minx = {minx}', f'maxy = {maxy}', 
        #       f'miny = {miny}')
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
    print((maxx - minx) * (maxy - miny))

# ex 1
minimal_bounding_rectangle_area([3,2,10,4],[5,5,3,2])

# ex 2
minimal_bounding_rectangle_area([2],[89])

# ex 3
minimal_bounding_rectangle_area([-8,8,9,-9,4,-4,4,-9,7],[10,1,-1,-5,7,-7,-2,0,3])