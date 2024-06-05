import random

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def bst_insert(T,k):
    if T == None:
        return Node(k)
    x = T
    while True:
        if k <= x.key:
            if x.left == None:
                x.left = Node(k)
                x.left.parent = x
                return T
            x = x.left
        else:
            if x.right == None:
                x.right = Node(k)
                x.right.parent = x
                return T
            x = x.right

def random_tree(n):
    t = None
    for i in range(n):
        t = bst_insert(t,random.randint(0,2*n))
    return t


def bst_walk(D, t):
    if t != None:
        bst_walk(D, t.left)
        D[t.key] = 1
        bst_walk(D, t.right)

# complexity of bst_walk: theta(n) because it visits all the nodes

def bst_subset(t1,t2):
    D1 = {}
    D2 = {}
    if t1 == None or t2 == None:
        return True
    bst_walk(D1, t1)
    bst_walk(D2, t2)
    print(D1)
    print('---')
    print(D2)
    for k in D1:
        if k in D2:
            D1[k] += 1
    print(D1)
    for k in D1:
        if D1[k] > 1:
            return True
    return False

# complexity of bst_subset: theta(n) because it visits all the nodes

