def median(a, b, c):
    if b >= a:
        a, b = b, a
    if c >= a:
        return a
    if c >= b:
        return c
    else:
        return b

# ex 1
print(median(1, 2, 3))

# ex 2
print(median(3, 2, 1))

# ex 3
print(median(7, 3, 21))

# ex 4
print(median(7, 3, 5))

# ex 5
print(median(7, 3, 3))

# ex 6
print(median(7, 3, 7))