#
# All algorithms are based on an adjacency list representation of a
# graph.  In practice, the vertexes are numbered from 0 to n-1.  These
# are the vertex identifiers used in the adjacency list.  We also
# store the names of the nodes in a 'Name' array.  In addition to
# these two containers, we use an index 'Idx' to map names to vertex
# ids.
#
# Name: (array) Vertex Id -> Vertex Name
# Adj: (array) Vertex Id -> array of Vertex Id
# Idx: (dictionary) Vertex Name -> Vertex Id
#
def read_graph(f):              # input in "adjacency-list format"
    Name = []                   # (see line format below)
    Adj = []
    Idx = {}
    for line in f:
        l = line.split()
        # 'A B C D' ==> ['A', 'B', 'C', 'D']
        # A->B, A->C, A->D
        # u  v  u  v  u  v
        if len(l) == 0:
            continue
        u_name = l[0]
        if u_name in Idx:
            u = Idx[u_name]
        else:
            u = len(Name)
            Name.append(u_name)
            Adj.append([])
            Idx[u_name] = u
        for i in range(1,len(l)):
            v_name = l[i]
            if v_name in Idx:
                v = Idx[v_name]
            else:
                v = len(Name)
                Name.append(v_name)
                Adj.append([])
                Idx[v_name] = v
            Adj[u].append(v)

    return Adj, Name, Idx

def all_dependencies (Adj, Name, Idx, p):
    S = []
    D = [False]*len(Adj)
    Q = [None]*len(Adj)
    Q_head = 0
    Q_tail = 0
    u = Idx[p]

    Q[Q_tail] = u               # enqueue(u)
    Q_tail += 1
    D[u] = True
    S.append(Name[u])
    while Q_tail != Q_head:     # loop while queue not empty
        u = Q[Q_head]
        Q_head += 1
        for v in Adj[u]:
            if D[v] == False:
                Q[Q_tail] = v
                Q_tail += 1
                D[v] = True
                S.append(Name[v])
    return S

def read_graph(f):              # input in "edge-list format"
    Name = []                   # (see line format below)
    Adj = []
    Idx = {}
    for line in f:
        l = line.strip().split('|')
        # 'EE|Estonia|LV|Latvia' ==> ['EE', 'Estonia', 'LV', 'Latvia']
        if len(l) != 4:
            continue
        u_name = l[1]
        v_name = l[3]
        if u_name in Idx:
            u = Idx[u_name]
        else:
            u = len(Name)
            Name.append(u_name)
            Adj.append([])
            Idx[u_name] = u
        if v_name != '':        # v_name is empty for an isolated node
            if v_name in Idx:
                v = Idx[v_name]
            else:
                v = len(Name)
                Name.append(v_name)
                Adj.append([])
                Idx[v_name] = v
            Adj[u].append(v)

    return Adj, Name, Idx

def count_connected_components(Adj, Name):
    n = len(Adj)                # number of vertexes in the graph
    D = [0]*n
    Q = [None]*n
    c = 0                       # number of connected components
    for u in range(n):
        if D[u] != 0:
            continue
        c = c + 1
        Q_head = 0
        Q_tail = 0
        Q[Q_tail] = u
        Q_tail += 1
        D[u] = c
        while Q_head != Q_tail:
            u = Q[Q_head]
            print (Name[u], end=' ')
            Q_head += 1
            for v in Adj[u]:
                if D[v] == 0:
                    D[v] = c
                    Q[Q_tail] = v
                    Q_tail += 1
        print()
    return c

# Non-recursive implementation of a depth-first search.  The main
# structure is the same as BFS, except that we use a stack to store
# and schedule the visitation of the "frontier" of the search.
def dfs (Adj):
    n = len(Adj)
    S = []                      # stack to store the "frontier" of the DFS exploration
    D = [0]*n                   # discovery "time" (0 == not yet discovered)
    F = [0]*n                   # finish "time" (0 == not yet finished)
    t = 1                       # "time" counter.
    for w in range(n):
        if D[w] != 0:           
            continue
        S.append(w)             # initiate a DFS from each vertex w 
        while len(S) > 0:       # that hasn't been discovered yet
            u = S[-1]

            if D[u] == 0:       # we see vertex u for the fist time:
                D[u] = t        # so we mark its discovery time
                t = t + 1       # and push onto the stack all its yet-undiscovered neighbors
                for v in Adj[u]:
                    if D[v] == 0:
                        S.append(v)
            elif F[u] == 0:     # we're done with u, so we mark its finish time
                F[u] = t        # and we pop it from the stack.
                t = t + 1
                S.pop()
            else:               # we might find an already finished node,
                S.pop()         # so we simply pop it from the stack.
    return D, F
