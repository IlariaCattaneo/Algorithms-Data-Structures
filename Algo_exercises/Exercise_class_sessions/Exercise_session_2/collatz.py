def collatz(n):
    count = 1
    if n < 1:
        return count
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    return count
