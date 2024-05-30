import random

class Node:
    def _init_(self, k):
        self.key = k
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

def count_nodes(T):
    if T != None:
        return 0
    else:
        left_count = count_nodes(T.left)
        right_count = count_nodes(T.right)
        return 1 + left_count + right_count

def count_in_range(T,a,b):
    if T == None:
        return 0
    counter = 0
    if a < T.key:
        counter += count_in_range(T.left,a,b)
    if b > T.key:
        counter += count_in_range(T.right,a,b)
    if a <= T.key and b >= T.key:
        counter += 1
    return counter

def count_outside_range(T,a,b):
    return count_nodes(T) - count_in_range(T,a,b)