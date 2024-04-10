def bst_height(tree):
    if tree is None:
        return 0
    return 1 + max(bst_height(tree.left), bst_height(tree.right))
