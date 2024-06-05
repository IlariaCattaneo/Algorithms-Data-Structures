def sums_one_two_three(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return sums_one_two_three(n-1) + sums_one_two_three(n-2) + sums_one_two_three(n-3)

# this is not efficient because it has an exponential complexity

def sums_one_two_three_better(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a = 1
        b = 2
        c = 4
        r = a + b + c
        for i in range(4,n):
            a = b
            b = c
            c = r
            r = a + b + c
        return r
    
# this is more efficient because it has a linear complexity

def test_sums_one_two_DP(n):
    DP = [0]*(n+1)
    DP[1] = 1
    DP[2] = 2
    DP[3] = 4
    for i in range(4,n+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    return DP[n]