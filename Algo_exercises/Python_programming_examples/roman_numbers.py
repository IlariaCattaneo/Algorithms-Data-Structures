ten_zero = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
ten_one = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
ten_two = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

def roman_numbers(n):
    assert n > 0
    global ten_zero, ten_one, ten_two

    r = ''
    while n >= 1000:
        r = r + 'M'
        n = n - 1000

    c = n // 100
    r = r + ten_two[c]
    n = n - c*100

    d = n // 10
    r = r + ten_one[d]
    n = n - d*10

    r = r + ten_zero[n]

    print(r)