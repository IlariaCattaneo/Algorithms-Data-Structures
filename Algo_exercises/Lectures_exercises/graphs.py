def read_graph(file):
    Name = []
    Adj = []
    Idx = {}
    for line in file:
        L = line.strip().split(' ')
        if len(L) == 0:
            continue
        u_name = L[0]
        if u_name not in Idx:
            Idx[u_name] = len(Name)
            Name.append(u_name)
            Adj.append([])
            u = len(Name) - 1
        else:
            u = Idx[u_name]
        for i in range(1,len(L)):
            v_name = L[i]
            if v_name not in Idx:
                Idx[v_name] = len(Name)
                Name.append(v_name)
                Adj.append([])
                v = len(Name) - 1
            else:
                v = Idx[v_name]
            Adj[u].append(v)
    return Name, Adj, Idx

def bfs(G, s):
    # G is the adjacency list, s is the idx of the node where we wnat to start from
    # we use a queue as data structure
    n = len(G)
    D = [None]*n # distance vector
    P = [None]*n # previous vector
    Q = [None]*n # queue
    Q_head = 0
    Q_tail = 0
    # enqueue s
    Q[Q_tail] = s
    Q_tail += 1
    D[s] = 0
    while Q_head != Q_tail:
        # dequeue
        u = Q[Q_head]
        Q_head += 1
        for v in G[u]:
            if D[v] == None: # i've not reached the node yet, I'm reaching it now
                D[v] = D[u] + 1
                P[v] = u
                # enqueue v
                Q[Q_tail] = v
                Q_tail += 1
    return D, P

def dfs(G):
    # we use a stack as data structure
    # G is the adjacency list
    # we use a stack as data structure
    n = len(G)
    D = [None]*n # discovery time vector
    F = [None]*n # finish time vector
    S = [] # stack
    t = 1 # time
    for u in range(n):
        if D[u] == None: # if we haven't discovered the node yet
            S.append(u)
            while len(S) > 0: # while stack is not empty
                u = S[-1]
                if D[u] == None:
                    D[u] = t
                    t += 1
                    for v in G[u]:
                        if D[v] == None:
                            S.append(v)
                elif F[u] == None:
                    F[u] = t
                    t += 1
                    S.pop()
                else:
                    S.pop()
    return D, F
