def distance_between_points(X, Y, d):
    minX = X[0]
    maxX = X[0]
    minY = Y[0]
    maxY = Y[0]
    assert len(X) == len(Y)
    for i in range(len(X)):
        if X[i] < minX:
            minX = X[i]
        elif X[i] > maxX:
            maxX = X[i]
        if Y[i] < minY:
            minY = Y[i]
        elif Y[i] > maxY:
            maxY = Y[i]
    if ((maxX-minX)**2 + (maxY-minY)**2)**0.5 >= d:
        return True
    return False

# ex 1
print(distance_between_points([3,2,1,10,5,4],[5,5,4,3,1,2],5))

# ex 2
print(distance_between_points([3,2,1,10,5,4],[5,5,4,3,1,2],1))

# ex 3
print(distance_between_points([3,2,1,10,5,4],[5,5,4,3,1,2],6))

# ex 4
print(distance_between_points([3,2,1,10,5,4],[5,5,4,3,1,2],4))