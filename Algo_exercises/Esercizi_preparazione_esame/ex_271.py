def check_connectivity(X,Y,r):
    n = len(X)
    D = [None]*n
    Q = [None]*n
    Q_head = 0
    Q_tail = 0
    # enqueue S
    Q[Q_tail] = (0,0)
    Q_tail += 1
    D[Q_tail] = True
    while Q_head != Q_tail:
        # dequeue S
        s = Q[Q_head]
        Q_head += 1
        for i in range(n):
            if D[i] == False and (X[s]-X[i])**2 + (Y[s]-Y[i])**2 <= r**2:
                D[i] = True
                # enqueue i
                Q[Q_tail] = (X[i], Y[i])
                Q_tail += 1
    for i in range(len(D)):
        if D[i] == False:
            return False
    return True