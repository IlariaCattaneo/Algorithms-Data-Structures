def distance_between_points(X,Y,d):
    i,j = 0,0
    maxx = X[0]
    minx = X[0]
    maxy = Y[0]
    miny = Y[0]
    while i < len(X) and j < len(Y):
        print(f'X[{i}] = {X[i]}', f'Y[{j}] = {Y[j]}', f'maxx = {maxx}', f'minx = {minx}', f'maxy = {maxy}', f'miny = {miny}')
        if X[i] > maxx:
            maxx = X[i]
        if X[i] < minx:
            minx = X[i]
        if Y[j] > maxy:
            maxy = Y[j]
        if Y[j] < miny:
            miny = Y[j]
        i += 1
        j += 1
    if maxx - minx >= d or maxy - miny >= d:
        return True
    else: return False