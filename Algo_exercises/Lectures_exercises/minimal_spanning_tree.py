def add_vertex(Adj, Name, Idx, u_name):
    if u_name not in Idx:
        Idx[u_name] = len(Name)
        Name.append(u_name)
        Adj.append([])
    else:
        u = Idx[u_name]
    return u

def read_weighted_undirected_graph(file):
    f = open(file, 'r')
    Name = []
    Adj = []
    Idx = {}
    for line in f:
        u_name, v_name, c = line.strip().split(' ')
        c = float(c)
        u = add_vertex(Adj, Name, Idx, u_name)
        v = add_vertex(Adj, Name, Idx, v_name)
        Adj[u].append((v, c))
        Adj[v].append((u, c))
    f.close()
    return Adj, Name, Idx

class disjoint_set:
    def __init__(self):
        self.parent = self

def set_find(set):
    while set.parent != set:
        set = set.parent
    return set

def set_union(set1, set2):
    set1 = set_find(set1)
    set2 = set_find(set2)
    set1.parent = set2

def krushkal(G):
    n = len(G)
    E = [] # list of edges of the graph
    for u in range(n):
        for v, c in G[u]:
            if u < v:
                E.append((c, u, v))
    E.sort()
    S = [None]*n
    for u in range(n):
        S[u] = disjoint_set(u)
    T = [None]*n # tree
    for u in range(n):
        T[u] = []
    for c, u, v in E:
        if set_find(S[u]) != set_find(S[v]):
            set_union(S[u], S[v])
            T[u].append((v, c))
            T[v].append((u, c))
    return T
            
def enqueue(Q, x):
    Q.append(x)
    i = len(Q) - 1
    while i > 0:
        p = (i-1)//2
        if Q[p] <= Q[i]:
            return
        Q[p], Q[i] = Q[i], Q[p]
        i = p 

def extract_min(Q):
    x = Q[0]
    Q[0] = Q[-1]
    Q.pop()
    i = 0
    while True:
        m = i 
        if 2*i + 1 < len(Q): # check the left child
            if Q[m] > Q[2*i + 1]:
                m = 2*i + 1
            if 2*i +2 < len(Q): # check the right child
                if Q[m] > Q[2*i + 2]:
                    m = 2*i + 2
        if m == i:
            return x
        Q[m], Q[i] = Q[i], Q[m]
        i = m        

def prim(G):
    n = len(G)
    T = [None]*n
    for u in range(n):
        T[u] = []
    Q = [] # priority queue
    enqueue(Q, (0.0, 0, None))
    V = [False]*n # visited
    while len(Q) != 0:
        c, v, u = extract_min(Q)
        if V[v]:
            continue
        if u != None:
            T[u].append((v, c))
            T[v].append((u, c))
            V[u] = True
        V[v] = True
        for w, c in G[v]:
            if not V[w]:
                enqueue(Q, (c, w, v))