def read_graph(f):
    """Read a graph from a file object 'f' (text) containing one
    vertex and its adjacency list per line.  E.g.:

    Input:     | Graph:
    A B C      |  A --> B
    B C        |  |    /^
    C B        |  v   / |
               |  C<-/  /
               |   ^---/

    Return three containers:

    V: (array) Vertex Id -> Vertex Name
    Adj: (array) Vertex Id -> array of Vertex Id
    V_idx: (dictionary) Vertex Name -> Vertex Id
    """
    V = []
    Adj = []
    V_idx = {}
    for line in f:              # for each line in the input f
        l = line.split()
        assert len(l) > 0
        v_name = l[0]           # v_name is the source vertex
        if v_name in V_idx:     # We already have vertex v_name
            v = V_idx[v_name]
        else:
            v = len(V)          # Add vertex at the end of V, Adj
            V_idx[v_name] = v
            V.append(v_name)
            Adj.append([])
        for i in range (1, len(l)):
            u_name = l[i]       # u_name is a target vertex
            if u_name in V_idx: # We already have vertex u_name
                u = V_idx[u_name]
            else:               # Add vertex, as above
                u = len(V)
                V_idx[u_name] = u
                V.append(u_name)
                Adj.append([])
            Adj[v].append(u)

    return V, Adj, V_idx
