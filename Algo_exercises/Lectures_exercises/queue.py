Q = [None] * 100
head = 0
tail = 0

def is_empty():
    global head, tail
    return head == tail

def next(i):
    i += 1
    if i == len(Q):
        return 0
    return i

def is_full():
    global head, tail
    return head == next(tail)

def enqueue(x):
    global Q, head, tail
    assert not is_full(), "Queue overflow"
    Q[tail] = x
    tail += 1

def dequeue():
    global Q, head, tail
    assert not is_empty(), "Queue underflow"
    head += 1
    return Q[head-1]
    