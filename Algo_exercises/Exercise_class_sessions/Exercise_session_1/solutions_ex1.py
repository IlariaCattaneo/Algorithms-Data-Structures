def median_value (a, b, c):
    if a > b:
        if c > a:
            return a
        elif c > b:
            return c
        else:
            return b
    else:
        if c > b:
            return b
        elif c > a:
            return c
        else:
            return a

def leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def classify_triangle(a,b,c):
    # it is convenient to first sort the three lengths, A, B, and C,
    # so that we can refer to the maximal length as a
    if b > a:
        a, b = b, a             # swap a <==> b
    if c > a:
        a, c = c, a             # swap a <==> c

    if a > b + c:
        print ('impossible')
    else:
        if a*a > b*b + c*c:
            angle = 'obtuse'
        elif a*a < b*b + c*c:
            angle = 'acute'
        else:
            angle = 'right'
        if a == b and b == c:
            sides = 'equilateral'
        elif a == b or b == c or a == c:
            sides = 'isosceles'
        else:
            sides = 'scalene'
        print (angle, sides)
