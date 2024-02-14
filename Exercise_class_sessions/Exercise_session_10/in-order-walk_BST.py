class Node:
    def __init__(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

def tree_insert (t, k):
# return the root of the tree we obtain from inserting a new node
# with key k into tree t
    if t == None:
        return Node(k)
    p = t
    while True:
        if k <= p.key:
            if p.left == None:
                p.left = Node(k)
                p.left.parent = p
                return t
            p = p.left
        else:
            if p.right == None:
                p.right = Node(k)
                p.right.parent = p
                return t
            p = p.right

def print_in_order(t):
    stack = []
    while True:
        if t != None:
            stack.append(t)
            t = t.left
        elif stack:
            t = stack.pop()
            print(t)
            t.right
        else:
            break
    



root = Node(10)
tree_insert(root, 5)
tree_insert(root, 11)
tree_insert(root, 4)
tree_insert(root, 8)
tree_insert(root, 6)
tree_insert(root, 9)
print_in_order(root)
