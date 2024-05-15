def bst_equals(t1,t2):
    if t1 == None and t2 == None:
        return True
    if t1.key == t2.key and bst_equals(t1.left,t2.left) and bst_equals(t1.right,t2.right):
        return True
    return False