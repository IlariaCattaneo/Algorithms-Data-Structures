def log_base_two(n):
    k = 0
    while 2**k <= n:
        k += 1
    return k - 1

# Ex 1
print(log_base_two(1))

# Ex 2
print(log_base_two(2))

# Ex 3
print(log_base_two(5))

# Ex 4
print(log_base_two(1000))
