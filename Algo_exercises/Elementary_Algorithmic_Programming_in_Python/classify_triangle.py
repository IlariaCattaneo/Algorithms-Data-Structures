def classify_triangle(a, b, c):
    # we sort in a descendent way
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a

    if a > b + c: # when the ipotenusa side is bigger than the sum of the other two cateti then it's impossible to build a triangle
        print('impossible')
    else:
        # to define angles we use pitagora a^2 + b^2 = c^2
        if a**2 > b**2 + c**2:
            angle = 'obtuse'
        elif a**2 < b**2 + c**2:
            angle = 'acute'
        else:
            angle = 'right'
        # to define sides we check the three numbers
        if a == b and b == c:
            side = 'equilateral'
        elif a == b or a == c or b == c:
            side = 'isoceles'
        else:
            side = 'scalene'
        print(angle, side)

# ex 1
classify_triangle(10, 10, 10)

# ex 2
classify_triangle(4, 3, 5)

# ex 3
classify_triangle(4, 3, 8)

# ex 4
classify_triangle(3, 4, 3)

# ex 5
classify_triangle(3, 5, 3)

# ex 6
classify_triangle(5, 5, 7)