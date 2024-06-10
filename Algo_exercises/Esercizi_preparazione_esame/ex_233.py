def has_cycle_len_4(G):
    for u in G:
        for v in G[u]:
            for w in G[v]:
                if w != u:
                    for z in G[w]:
                        if z != v:
                            for x in G[z]:
                                if x == u:
                                    return True
    return False