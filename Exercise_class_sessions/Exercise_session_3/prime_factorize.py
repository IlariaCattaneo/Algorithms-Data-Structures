def prime_factorize(n):
    """Returns a list of the prime factors for a natural number."""
    if n <= 0 :
        raise ValueError ( "n must be > 0" )
    factors = []
    d = 2
    while n > 1 :
        while n % d == 0 :
            factors.append ( d )
            n /= d
        d = d + 1
        if d*d > n :
            if n > 1 : factors.append ( int(n) )
            break
    if(len(factors) == 0):
        return ""
    elif(len(factors) == 1):
        return f"{factors[0]}"
    """E notations used to represent large numbers."""
    s = ""
    count = 1
    f = 1
    while f < len(factors):
        if(factors[f] == factors[f-1]):
            count += 1
        else:
            if(count == 1):
                s += f"{factors[f-1]} "
            else:
                s += f"{factors[f-1]}E{count} "
            count = 1
        f += 1
    if( count == 1 ):
        s += f"{factors[f-1]} "
    else:
        s+= f"{factors[f-1]}E{count} "
    return s.strip()