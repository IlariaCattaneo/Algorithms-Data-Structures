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

    Name: (array) Vertex Id -> Vertex Name
    Adj: (array) Vertex Id -> array of Vertex Id
    Idx: (dictionary) Vertex Name -> Vertex Id
    """
    Name = []
    Adj = []
    Idx = {}
    for line in f:              # for each line in the input f
        l = line.strip().split()
        assert len(l) > 0
        u_name = l[0]           # v_name is the source vertex
        if u_name in Idx:       # We already have vertex v_name
            u = Idx[v_name]
        else:
            u = len(Name)       # Add vertex at the end of Name, Adj
            Idx[u_name] = u
            Name.append(u_name)
            Adj.append([])
        for i in range (1, len(l)):
            v_name = l[i]       # u_name is a target vertex
            if v_name in Idx:   # We already have vertex v_name
                v = Idx[v_name]
            else:               # Add vertex, as above
                v = len(Name)
                Idx[v_name] = v
                Name.append(v_name)
                Adj.append([])
            Adj[u].append(v)

    return Name, Adj, Idx


# Count connected components BFS
def bfs(G, start, visited):
    n = len(G)
    Q = [None]*n
    Q_head = 0
    Q_tail = 0
    Q[Q_tail] = start
    Q_tail += 1
    visited[start] = True
    while Q_head != Q_tail:
        vertex = Q[Q_head]
        Q_head += 1
        for neighbor in G[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                Q[Q_tail] = neighbor
                Q_tail += 1

def count_connected_components_bfs(G):
    n = len(G)
    count = 0
    visited = [False]*n
    for vertex in range(n):
        if not visited[vertex]:
            bfs(G, vertex, visited)
            count += 1
    return count

# Count connected components DFS
def dfs(G, vertex, visited):
    stack = [vertex]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for neighbor in G[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def count_connected_components_dfs(G):
    n = len(G)
    count = 0
    visited = [False] * n
    for vertex in range(n):
        if not visited[vertex]:
            dfs(G, vertex, visited)
            count += 1
    return count

# Topological sort
def dfs_topological_sort(G, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            dfs_topological_sort(G, neighbor, visited, stack)
    stack.append(vertex)

def topological_sort(G):
    n = len(G)
    visited = [False] * n
    stack = []
    for vertex in range(n):
        if not visited[vertex]:
            dfs_topological_sort(G, vertex, visited, stack)
    return stack[::-1]  # Return reversed stack as the topological order


# ADDITIONAL EXERCISES
# Check if a graph is cyclic
def dfs_cycle(G, vertex, visited, parent):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            if dfs_cycle(G, neighbor, visited, vertex):
                return True
        elif neighbor != parent:
            return True
    return False

def is_cyclic(G):
    n = len(G)
    visited = [False] * n
    for vertex in range(n):
        if not visited[vertex]:
            if dfs_cycle(G, vertex, visited, -1):
                return True
    return False

# Hop distance between two nodes
def hop_distance(G, start, target):
    if start == target:
        return 0
    n = len(G)
    visited = [False] * n
    D = [None] * n
    Q = [None] * n
    Q_head = 0
    Q_tail = 0
    Q[Q_tail] = start
    Q_tail += 1
    visited
    D[start] = 0
    while Q_head != Q_tail:
        vertex = Q[Q_head]
        Q_head += 1
        for neighbor in G[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                D[neighbor] = D[vertex] + 1
                if neighbor == target:
                    return D[neighbor]
                Q[Q_tail] = neighbor
                Q_tail += 1
    return None

