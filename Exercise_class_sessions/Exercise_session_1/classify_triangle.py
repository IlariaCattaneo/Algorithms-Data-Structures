# given three positive numbers representing the lengths of three segments, respectively, 
# output a classification of the triangle obtained by connecting the three segments. 
# The output consists of one or two words printed on a single line and separated by a single space. 
# The first word is one of acute, right, obtuse, or impossible. impossible indicates that it is 
# impossible to form a triangle with the given segment lengths, in which case the output ends there. 
# Acute, right, and obtuse indicate that the resulting triangle has all acute angles, one right angle, or one obtuse angle. 
# In these cases, the output must contain a second word that can be either scalene, isosceles, or equilateral, indicating the type of triangle.

# trova il lato piu lungo 
# se il quadrato del piu lungo è uguale alla somma dei quadrati degli altri due = il triangolo è rettangolo (ha un angolo retto e due acuti)
# se è minore il triangolo ha solo angoli acuti 
# se è maggiore il triangolo ha un angolo ottuso e due acuti 
# qualunque lato deve essere <= alla somma degli altri due lat

# se due lati sono uguali = isoscele
# se lati sono tutti diversi = scaleno
# se lati sono tutti uguali = equilatero

def classify_triangle(a, b, c):
    m = max(a, b, c)

    if a > (b + c) or b > (a + c) or c > (a + b):
        print("impossible")
    elif m == a:
        if m^2 == (b^2 + c^2):
            if a == b or a == c or b == c:
                print("right isosceles")
            elif a != b and a != c and b != c:
                print("right scalene")
        elif m^2 < (b^2 + c^2): 
            if a == b or a == c or b == c:
                print("acute isosceles")
            elif a == b and a == c:
                print("acute equilateral")
            elif a != b and a != c and b != c:
                print("acute scalene")
        elif m^2 > (b^2 + c^2):
            if a == b or a == c or b == c:
                print("obtuse isosceles") 
            elif a != b and a != c and b != c:
                print("obtuse scalene")
    elif m == b:
        if m^2 == (a^2 + c^2):
            if a == b or a == c or b == c:
                print("right isosceles") 
            elif a != b and a != c and b != c:
                print("right scalene")
        elif m^2 < (a^2 + c^2): 
            if a == b or a == c or b == c:
                print("acute isosceles")
            elif a == b and a == c:
                print("acute equilateral")
            elif a != b and a != c and b != c:
                print("acute scalene")
        elif m^2 > (a^2 + c^2):
            if a == b or a == c or b == c:
                print("obtuse isosceles") 
            elif a != b and a != c and b != c:
                print("obtuse scalene")
    elif m == c:
        if m^2 == (b^2 + a^2):
            if a == b or a == c or b == c:
                print("right isosceles") 
            elif a != b and a != c and b != c:
                print("right scalene")
        elif m^2 < (b^2 + a^2): 
            if a == b or a == c or b == c:
                print("acute isosceles")
            elif a == b and a == c:
                print("acute equilateral")
            elif a != b and a != c and b != c:
                print("acute scalene")
        elif m^2 > (a^2 + b^2):
            if a == b or a == c or b == c:
                print("obtuse isosceles") 
            elif a != b and a != c and b != c:
                print("obtuse scalene")
