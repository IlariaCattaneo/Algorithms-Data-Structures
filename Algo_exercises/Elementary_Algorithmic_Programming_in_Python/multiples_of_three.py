def multiples_of_three(A):
    counter = 0
    for number in A:
        if number % 3 == 0:
            counter += 1
    print(counter)

# ex 1
multiples_of_three([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40])

# ex 2
multiples_of_three([7, 2, 0])