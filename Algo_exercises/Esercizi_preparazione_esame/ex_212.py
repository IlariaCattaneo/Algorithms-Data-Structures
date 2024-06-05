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

def count_full_nodes(t):
    if t == None:
        return 0
    count = 0
    if t.left != None and t.right != None:
        count += 1
    count += count_full_nodes(t.left) + count_full_nodes(t.right)
    return count

# complexity: theta(n)

def right_rotate(x):
    l = x.left
    x.left = l.right
    l.right = x
    return l

def no_full_nodes(t):
    if t == None:
        return t
    if t.left == None:
        t.right = no_full_nodes(t.right)
        return t
    elif t.right == None:
        t.left = no_full_nodes(t.left)
        return t
    while t.left != None:
        t = right_rotate(t)
    t.right = no_full_nodes(t.right)
    return t