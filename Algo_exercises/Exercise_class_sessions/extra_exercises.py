def fibonacci(n):
    sequence = []
    a, b = 0, 1
    sequence.append(a)
    sequence.append(b)
    while len(sequence) < n:
        c = sequence[a] + sequence[b]
        sequence.append(c)
        a += 1
        b += 1
    return sequence


def factorial(n):
    fact = 1
    if n == 1:
        print(fact)
    else:    
        while n > 0:
            fact = fact * n
            n -= 1
        print(fact)

def unique_characters(string):
    letters = []
    for letter in string:
        if letter not in letters:
            letters.append(letter)
        else:
            return False
    return True

def determinant(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    return a*d - b*c

def compress_string(string):
    if not string:
        return ''
    compressed = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed.append(string[i - 1] + str(count))
            count = 1
    compressed.append(string[-1] + str(count))
    compressed_string = ''.join(compressed)
    if len(compressed_string) < len(string):
        return compressed_string  
    else:
        return string