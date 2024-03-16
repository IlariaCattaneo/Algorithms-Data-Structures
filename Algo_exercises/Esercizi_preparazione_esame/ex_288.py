def algo_y(T):
    x = 0
    for i in range(len(T)):
        l = T[i].amount
        r = T[i].amount
        for j in range(len(T)):
            if i != j:
                if T[j].date <= T[i].date and T[i].date - T[j].date <= 10:
                    l += T[j].amount
                if T[j].date >= T[i].date and T[j].date - T[i].date <= 10:
                    r += T[j].amount
        if x < r:
            x = r
        if x < l:
            x = l
    return x

# algo_y returns the maximum total amount that is gathered in a 10 days interval
# worst case complexity: theta(n^2) -> the function needs to scan the entire array for each transaction
# best case complexity: theta(n^2) -> the function still need to scan the entire array for each transaction

def better_algo_y(T):
    max_amount = 0
    tmp_amount = 0
    S = sorted(T, key=lambda x: x.date)
    i, j = 0, 0
    while j < len(S):
        if S[j].date - S[i].date <= 10:
            tmp_amount += S[j].amount
            j += 1
            if tmp_amount > max_amount:
                max_amount = tmp_amount
        else:
            i += 1
            j = 1
    return max_amount
        