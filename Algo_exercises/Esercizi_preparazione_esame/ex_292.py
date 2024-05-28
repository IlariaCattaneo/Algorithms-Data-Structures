def minimal_cost_game(A,B):
    return DP(A,0,B,0,{})

def value(card):
    return card[0]

def suit(card):
    return card[1]

def DP(A,i,B,j,memo):
    if i == len(A) and j == len(B):
        return 0
    if (i,j) in memo:
        return memo[(i,j)]
    if i == len(A): # if we have no more cards in A
        m = 0
        while j < len(B):
            m += value(B[j])
            j += 1
        memo[(i,j)] = m
        return m
    if j == len(B): # if we have no more cards in B
        m = 0
        while i < len(A):
            m += value(A[i])
            i += 1
        memo[(i,j)] = m
        return m
    m = min(value(A[i]) + DP(A,i+1,B,j,memo), value(B[j]) + DP(A,i,B,j+1,memo)) # we can choose the min of the card from A or B
    if value(A[i]) == value(B[j]) or suit(A[i]) == suit(B[j]): # if the cards have the same value or suit
        m = min(m, DP(A,i+1,B,j+1,memo)) # we can choose min of the two cards
    memo[(i,j)] = m
    return m