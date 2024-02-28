def prime_factors(n):
    assert n > 0
    # a**j * b**k == n
    # factorization is with prime numbers elevated to some power
    prime_factors = []
    while n % 2 == 0:
        n = n // 2
        prime_factors.append(2)
        if n == 1:
            break
    for factor in range(3, n+1):
        while n % factor == 0:
            n = n // factor
            prime_factors.append(factor)
            if n == 1:
                break

    factors = {}
    for number in prime_factors:
        if number in factors:
            factors[number] += 1
        else:
            factors[number] = 1
    print(factors)

    for key,value in factors.items():
        if value == 1:
            print(key)
        else:
            print(f'{key}^{value}')