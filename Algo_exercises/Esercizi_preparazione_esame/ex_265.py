def max_heap_insert(H, x):
    H.heap_size += 1
    i = H.heap_size
    H[i] = x
    while i > 1 and H[i] > H[i//2]:
        H[i], H[i//2] = H[i//2], H[i]
        i = i//2

# [3, 7, 3, 2, 9, 5, 9, 8, 5, 2, 9, 4, 7, 3, 9]
# [9, 9, 9, 7, 8, 7, 9, 2, 5, 2, 3, 3, 4, 3, 5]