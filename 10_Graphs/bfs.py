V = []                          # vertexes 
Adj = []                        # adjacency list
V_idx = {}                      # index: name --> vertex_id

#
# Exercise: read a graph from the input in the following format:
#
# v | Adj(v)
# ------------
# TI VS UR GR  # A = [ 'TI', 'VS', 'UR', 'GR' ]
# UR TI GR VS
# GR TI UR
# VS TI

import sys

for line in sys.stdin:
    A = line.strip().split()
    for v in A:
        # v is a string, vertex name
        if not v in V_idx:
            V_idx[v] = len(V)
            V.append(v)
            Adj.append([])
    v_i = V_idx[A[0]]
    for i in range(1,len(A)):
        u_i = V_idx[A[i]]
        Adj[u_i].append(v_i)
        Adj[v_i].append(u_i)

print(Adj)

n = len(V)

# BFS(G,0)
Visited = [False]*n
Q = [0]
head = 0
Visited[0] = True
count = 1
print(V[0])
while head < len(Q):
    v = Q[head]
    head = head + 1
    for u in Adj[v]:
        if not Visited[u]:
            print(V[u])
            Visited[u] = True
            Q.append(u)
            count = count + 1

if count == n:
    print('connected')
else:
    print('disconnected')

