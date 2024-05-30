def maximal_connected_subgraph(G):
    n = len(G)
    C = [None]*n
    m = 0
    max_c = None
    for v in G: # for vertex in list of vertices
        if C[v] == None:
            Q = [None]*n
            Q_head, Q_tail = 0, 0
            Q[Q_tail] = v
            Q_tail += 1
            C[v] = v
            count = 0
            while Q_head != Q_tail:
                u = Q[Q_head]
                Q_head += 1
                count += 1
                for w in G[u]: # for vertex w in the adjacency list of v
                    if C[w] == None:
                        Q[Q_tail] = w
                        Q_tail += 1
                        C[w] = v
            if count > m:
                m = count
                max_c = v
            for v in G: # for vertex in list of vertices
                if C[v] == max_c:
                    print(v)