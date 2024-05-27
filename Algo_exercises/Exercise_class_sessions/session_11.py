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
    if n == 0:
        return 0
    if n == 1:
        return A[0]
    dp = [0] * n

    # Initialize the base cases
    dp[0] = max(0, A[0])  # If only one element, either take it or leave it (0 if negative)
    dp[1] = max(dp[0], A[1])  # Either take the first element or the second one

    # Fill the dp array
    for i in range(2, n):
        dp[i] = max(dp[i - 1], A[i] + dp[i - 2])

    return dp[-1]
