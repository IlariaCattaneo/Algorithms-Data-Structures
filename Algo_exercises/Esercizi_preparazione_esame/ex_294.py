def minimal_additional_edges(G):
    n = len(G)
    C = [None]*n
    count = 0
    for v in G: # for vertex in list of vertices
        if C[v] == None:
            Q = [None]*n
            Q_head, Q_tail = 0,0
            Q[Q_tail] = v
            Q_tail += 1
            C[v] = v
            count += 1
            while Q_head != Q_tail:
                u = Q[Q_head]
                Q_head += 1
                count += 1
                for w in G[u]:
                    if C[w] == None:
                        Q[Q_tail] = w
                        Q_tail += 1
                        C[w] = v
    return count - 1