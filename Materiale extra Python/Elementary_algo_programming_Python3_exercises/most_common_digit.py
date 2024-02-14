# Write a function called  most_common_digit(n) that takes an integer , and returns
# the most common digit in the decimal representation of n. If there are two or more most
# common digits, the function must return the smallest one

def most_common_digit(n):
    count = 0
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i] == n[j]:
                count = count + 1