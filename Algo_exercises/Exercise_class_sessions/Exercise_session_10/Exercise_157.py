class Node:
    def __init__(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

def BST_insert(t, k):
    if t == None:
        return Node(k)
    elif k <= t.key:
        t.left = BST_insert(t.left, k)
    else:
        t.right = BST_insert(t.right, k)
    return t

def sort_for_balanced_BST(A):
    if A.key == None:
        height = None
    elif A.left == None and A.right == None:
        height = 0
    else:
        left_height = sort_for_balanced_BST(A.left)
        right_height = sort_for_balanced_BST(A.right)
        max_height = max(left_height, right_height) + 1

# the height of a tree is the length of the longest path from the root to a leaf


# Write an algorithm Sort-For-Balanced-BST(A) that takes an array of numbers A, and
# prints the elements of A in a new order so that, if the printed sequence is passed to BST-
# Insert, the resulting BST would be of minimal height. Also, analyze the complexity of your
# solution.