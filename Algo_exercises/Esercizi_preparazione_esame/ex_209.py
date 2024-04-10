def is_max_heap(heap):
    for i in range(len(heap)//2):
        if heap[i] < heap[2*i] or heap[i] < heap[2*i+1]:
            return False
    return True

def is_min_heap(heap):
    for i in range(len(heap)//2):
        if heap[i] > heap[2*i] or heap[i] > heap[2*i+1]:
            return False
    return True

def heap_properties(heap):
    max = is_max_heap(heap)
    min = is_min_heap(heap)
    if max and not min:
        return 1
    elif not max and min:
        return -1
    elif max and min:
        return 2
    else:
        return 0