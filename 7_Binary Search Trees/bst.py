class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def bst_insert(t, x):
    if t == None:
        return Node(x)
    root = t
    while True:
        if t.key >= x:
            if t.left == None:
                t.left = Node(x)
                return root
            t = t.left
        else:
            if t.right == None:
                t.right = Node(x)
                return root
            t = t.right
    
def bst_search(t, x):
    while t != None:
        if x < t.key:
            t = t.left
        elif x > t.key:
            t = t.right
        else:
            return True
    return False

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

def tree_min(t):
    if t != None:
        while t.left != None:
            t = t.left
        return t.key

def tree_max(t):
    if t != None:
        while t.right != None:
            t = t.right
        return t.key

def random_tree(n):
    t = None
    for i in range(n):
        t = bst_insert(t,random.randint(0,2*n))
    return t

def right_rotate(t):
    assert t != None
    assert t.left != None
    i = t.left
    t.left = i.right
    i.right = t
    return i
