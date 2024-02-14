# Write a function called  find_a_square(X,Y) that, given two arrays of coordinates X
# and Y representing n points, and a number d, return True if and only if four of those
# points are the vertices of a square, or False otherwise

def find_a_square(X,Y):
    for i in range(len(X)):
        for j in range(i+1,len(X)):
            for k in range(j+1,len(X)):
                for l in range(k+1,len(X)):
                    if (X[i] - X[j])**2 + (Y[i] - Y[j])**2 == (X[i] - X[k])**2 + (Y[i] - Y[k])**2 == (X[i] - X[l])**2 + (Y[i] - Y[l])**2 == (X[j] - X[k])**2 + (Y[j] - Y[k])**2 == (X[j] - X[l])**2 + (Y[j] - Y[l])**2 == (X[k] - X[l])**2 + (Y[k] - Y[l])**2:
                        return True
    return False