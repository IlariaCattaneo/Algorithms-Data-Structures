from math import isqrt

def sums_of_squares(n):
    for a in range(isqrt(n) + 1):
        b_squared = n - a**2
        b = isqrt(b_squared)
        if a**2 + b**2 == n and a <= b:
            print(f'{a**2} + {b**2} = {n}')

# ex 1
sums_of_squares(25)

# ex 2
sums_of_squares(21)

# ex 3
sums_of_squares(125)

# ex 4
sums_of_squares(178)

# ex 5
sums_of_squares(179)

# ex 6
sums_of_squares(17993241)