def leap_year(y):
    if y % 4 == 0 and (y % 400 == 0 or not y % 100 == 0):
        return True
    else:
        return False
    
    
# ex 1
print(leap_year(2000))

# ex 2
print(leap_year(1969))

# ex 3
print(leap_year(2023))

# ex 4
print(leap_year(1984))

# ex 5
print(leap_year(2022))

# ex 6
print(leap_year(2200))

# ex 7
print(leap_year(2400))

# ex 8
print(leap_year(1900))