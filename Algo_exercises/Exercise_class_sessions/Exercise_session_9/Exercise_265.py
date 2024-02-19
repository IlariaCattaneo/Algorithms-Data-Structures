# Write an algorithm  Max-Heap-Insert(H, x)  that inserts a value x in a max-heap H.
# Also, write the content of H (as an array) after the insertion of each of the following
# values, in the given order, starting from an empty max-heap: 3, 7, 3, 2, 9, 5, 9, 8, 5, 2, 9,
# 4, 7, 3, 9

def Max_Heap_Insert(H, x):
    H.append(x)
    # heapsort