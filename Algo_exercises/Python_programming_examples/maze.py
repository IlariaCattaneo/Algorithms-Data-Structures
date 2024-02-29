import random
def generate_maze(height, length):
    walls = '\\/'
    for i in range(height):
        row = ''
        for j in range(length):
            row += random.choice(walls)
        print(row)

generate_maze(20, 60)

