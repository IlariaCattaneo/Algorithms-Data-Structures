def bst_find_sum(t, v):
    t1 = bst_min(t)
    while t1 != None:
        t2 = bst_search(t, v-t1.key)
        if t2 != None:
            return t1, t2
        else:
            t1 = bst_successor(t1)
    return None
# wc complexity: theta(n^2)

def bst_min(t):
    if t != None:
        while t.left is not None:
            t = t.left
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
