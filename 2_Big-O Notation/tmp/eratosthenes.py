def sieve_of_eratosthenes(n):
    #creates an array of booleans
    P = [True] * (n + 1)
    P[0] = False
    P[1] = False
    i = 2
    while i*i < len(P):
        #test wheteher P[i] is true
        if P[i] == True:
            #i is our initial prime, so we cross out all the multiples of i
            j = i * i
            while j < len(P):
                P[j] = False
                j += i
        i += 1
    return P

