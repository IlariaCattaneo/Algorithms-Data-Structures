class Obj:
    def __init__(self, category, weight):
        self.category = category
        self.weight = weight

def algo_x(A):
    c  = A[1].category
    w = float('-inf')
    for i in range(len(A)):
        t = 0
        for j in range(i,len(A)):
            if A[j].category == A[i].category:
                t += A[j].weight
        if t > w or (t == w and A[i].category < c):
                c = A[j].category
                w = t
    return c

# complexity is theta(n^2)
# returns the category with the highest weight sum if it there only 1 category with the highest weight sum
# otherwise, if there is more than 1 category with the same weight sum, it returns the category with the lowest category number

def better_algo_x(A):
    D = {}
    for i in range(len(A)):
        if A[i].category not in D:
            D[A[i].category] = A[i].weight
        else:
            D[A[i].category] += A[i].weight
    print(D)
    max = float('-inf')
    cat = A[1].category
    for key,value in D.items():
        if value > max or (value == max and key < cat):
            max = value
            cat = key
    return cat

# complexity is theta(n)