def C(A):
    C = [1]*10
    for number in A:
        C[number%10] += 1
    r = 1
    for i in C:
        r = r * i
    return r - 1

def print_C(A):
    C = []
    for i in range(10):
        C.append([''])
    for number in A:
        C[number%10].append(number)
    I = [0]*10
    i = 0
    while True:
        # print the set corresponding to the indexs in I
        for j in range(10):
            if C[j][I[j]] != None:
                print(C[j][I[j]], end = ' ')
        print()
        # increment the indexes in I
        while True:
            I[i] += 1
            if I[i] < len(C[i]):
                break
            I[i] = 0
            i += 1
            if i == 10:
                return
        i = 0