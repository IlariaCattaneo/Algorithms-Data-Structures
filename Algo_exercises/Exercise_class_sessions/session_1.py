def rotation(x, y):
    z = x
    x = -y
    print(x, z)

def linear_transformation(x, y):
    x1 = 2*x
    y1 = x + y
    print(x1, y1)

def half_adder(a, b):
    if a == 1 and b == 1:
        s = 0
        c = 1
    elif (a == 0 and b == 1) or (a == 1 and b == 0):
        s = 1
        c = 0
    elif a == 0 and b == 0:
        s = 0
        c = 0
    print(s, c)

def full_adder(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                s = 0
            else:
                s = 1
                c = 0
        else:
            if c == 0:
                s = 1
            else:
                s = 0
                c = 1
    else:
        if b == 0:
            if c == 0:
                s = 1
            else:
                s = 0
                c = 1
        else:
            if c == 0:
                s = 0
                c = 1
            else:
                s = 1
                c = 1
    print(s, c)



# ex rotation
rotation(1, 1)

# ex linear transformation
linear_transformation(7, 2)

# ex half adder
half_adder(0, 1)
half_adder(1, 1)

# ex full adder
full_adder(1, 0, 1)