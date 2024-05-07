import random

class Node:
    def _init_(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

def bst_in_order_walk(t):
    if t is not None:
        bst_in_order_walk(t.left)
        print(t.key)
        bst_in_order_walk(t.right)

def bst_min(t):
    if t != None:
        while t.left is not None:
            t = t.left
    return t.key

def bst_max(t):
    if t != None:
        while t.right != None:
            t = t.right
        return t.key

def bst_successor(t):
    if t is None:
        return None
    if t.right is not None:
        return bst_min(t.right)
    p = t.parent
    while p is not None and t == p.right:
        t = p
        p = p.parent
    return p

def bst_search(t, k):
    while t != None:
        if k < t.key:
            t = t.left
        elif k > t.key:
            t = t.right
        else:
            return True
    return False

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

def bst_delete(T,z):
    if z.left == None or z.right == None:
        y = z
    else:
        y = bst_successor(z)
    if y.left != None:
        x = y.left
    else:
        x = y.right
    if x != None:
        x.parent = y.parent
    if y.parent == None:
        T = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
    if y != z:
        z.key = y.key
    return T

def bst_height(T):
    max = 0
    while T != None:
        if T.left != None and bst_height(T.left) > max:
            max = bst_height(T.left)
        if T.right != None and bst_height(T.right) > max:
            max = bst_height(T.right)
        return max + 1
    
def bst_count_in_range(T,a,b):
    if T == None:
        return 0
    c = 0
    if a < T.key:
        c = c + bst_count_in_range(T.left,a,b)
    if b > T.key:
        c = c + bst_count_in_range(T.right,a,b)
    if a <= T.key and b >= T.key:
        c = c + 1
    return c

def bst_expected_height(n,M):
    A = [i for i in range(n)]
    sum = 0
    for _ in range(M):
        random.shuffle(A)
        T = None
        for a in A:
            T = bst_insert(T,a)
        sum += bst_height(T)
    return sum/M

def bst_random(n):
    A = [i for i in range(n)]
    random.shuffle(A)
    T = None
    for a in A:
        T = bst_insert(T,a)
    return T

def random_tree(n):
    t = None
    for i in range(n):
        t = bst_insert(t,random.randint(0,2*n))
    return t

def left_rotation(t):
    assert t != None
    assert t.right != None
    i = t.right
    t.right = i.left
    i.left = t
    return i

def right_rotation(t):
    assert t != None
    assert t.left != None
    i = t.left
    t.left = i.right
    i.right = t
    return i

def root_insert(T,z):
    if T == None:
        return z
    if z.key < T.key:
        T.left = root_insert(T.left, z) 
        return right_rotation(T)
    else:
        T.right = root_insert(T.right, z)
        return left_rotation(T)
    
def print_in_order(t):
    if t != None:
        print_in_order(t.left)
        print(t.key)
        print_in_order(t.right)

def print_in_reverse_order(t):
    if t != None:
        print_in_reverse_order(t.right)
        print(t.key)
        print_in_reverse_order(t.left)