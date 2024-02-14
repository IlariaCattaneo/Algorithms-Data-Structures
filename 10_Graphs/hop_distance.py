#!/usr/bin/python3

V = []                          # vertexes 
Adj = []                        # adjacency list
V_idx = {}                      # index: name --> vertex_id

#
# Exercise: read a graph from the input in the following format:
#
# v | Adj(v)
# ------------
# TI VS UR GR
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

n = len(V)

src = 0

# BFS(G,s)

Visited = [False]*n
D = [None]*n                    # distances from the source node src
P = [None]*n
# 
D[src] = 0
P[src] = src                    # by definition -- doesn't make much sense anyway
#
Q = [src]
head = 0
Visited[0] = True
#
while head < len(Q):
    v = Q[head]
    head = head + 1
    for u in Adj[v]:
        if not Visited[u]:
            P[u] = v
            D[u] = D[v] + 1
            Visited[u] = True
            Q.append(u)

for i in range(n):
    print('node',V[i],'is at distance',D[i],'from node',V[src])
