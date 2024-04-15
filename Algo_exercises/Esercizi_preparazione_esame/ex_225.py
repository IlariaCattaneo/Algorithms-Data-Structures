def pq_init(n):
    # create a queue
    Q = [None] * n
    Q.size = 0
    Q.max_size = n
    return Q

def pq_enqueue(Q, x):
    if Q.size == Q.max_size:
        return False
    Q[Q.size] = x
    i = Q.size
    Q.size += 1
    while i > 1 and Q[i] < Q[i//2]:
        Q[i], Q[i//2] = Q[i//2], Q[i]
        i = i//2

def pq_dequeue(Q):
    if Q.size == 0:
        return False
    x = Q[0]
    Q[0], Q[Q.size] = Q[Q.size], Q[0]
    Q.size += 1
    i = 0
    while 2*i < Q.size:
        j = i
        m = Q[i]
        if Q[2*i] > m:
            j = 2*i
            m = Q[2*i]
        if 2*i+1 <= Q.size and Q[2*i+1] > m:
            j = 2*i+1
            m = Q[2*i+1]
        if j > i:
            Q[i], Q[j] = Q[j], Q[i]
            i = j
        else:
            return x
    return x