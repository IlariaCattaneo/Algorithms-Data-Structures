# Write a function called sums_of_squares(n) that prints all the pairs of squares that
# sum to n. That is, sums_of_squares(n) prints a line a^2 + b^2 for all the distinct pairs 
# a <= b such that a^2 + b^2 = n.

def sums_of_squares(n):
    for a in range(n):
        for b in range(n):
            if a**2 + b**2 == n:
                print(a, b)
                