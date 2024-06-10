def verify(G,k,S):
    # S is a sequence of verteces, that should be in G
    if len(S) != k:
        return False
    S.append(S[0])
    for vertex in range(len(S)-1):
        if S[vertex] not in G and S[vertex+1] not in G:
            return False
    return True