# BEST CARD GAME
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

# MAXIMAL NON-ADJACENT SUM
def max_adjacent_sum(A):
    n = len(A)
    DP = [0] * (n+2)
    for i in range(n+2,-1,-2):
        DP[i] = max(A[i] + DP[i+2], DP[i+1])
    return DP[0]

def dp_memoization(M,A,i):
    if i >= len(A):
        return 0
    if i in M:
        return M[i]
    m = max(A[i] + dp_memoization(M,A,i+2), dp_memoization(M,A,i+1))
    M[i] = m
    return m

def dp_recursive(A,i):
    if i >= len(A):
        return 0
    return max(A[i] + dp_recursive(A,i+2), dp_recursive(A,i+1))