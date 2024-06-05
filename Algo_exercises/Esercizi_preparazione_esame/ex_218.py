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

def bst_equals(t1,t2):
    if t1 == None and t2 == None:
        return True
    if t1.key == t2.key and bst_equals(t1.left,t2.left) and bst_equals(t1.right,t2.right):
        return True
    return False

# complexity of bst_equals: theta(n) because it visits all the nodes

def bst_walk(T,t):
    if t != None:
        bst_walk(T,t.left)
        T.append(t.key)
        bst_walk(T,t.right)

def bst_equal_keys(t1,t2):
    if t1 == None and t2 == None:
        return True
    T1 = []
    T2 = []
    bst_walk(T1, t1)
    bst_walk(T2, t2)
    if len(T1) != len(T2):
        return False
    T1.sort()
    T2.sort()
    for i in range(len(T1)):
        if T1[i] != T2[i]:
            return False
    return True

# complexity of bst_equal_keys: theta(nlogn) because of the sorting
# complexity of bst_walk: theta(n)