A = [0]
while True:
    line = input()
    if line == '':
        break
    for x in line.split():
        A.append(int(x))
