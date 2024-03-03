def partition(n, limit, P):
    assert n >= limit
    while limit > 0:
        P.append(limit)
        remainder = n - limit
        if remainder > limit:
            partition(remainder, limit, P)
        else:
            if remainder == 0:
                for n in P:
                    print(n,end=' ')
                print()
            else:
                partition(remainder, remainder, P)
        del P[-1]
        limit -= 1