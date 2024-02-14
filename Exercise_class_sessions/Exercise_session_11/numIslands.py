import sys

class Node:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

# grid = [
# ["1","1","1","1","0"],
# ["1","1","0","1","0"],
# ["1","1","0","0","0"],
# ["0","0","0","0","0"]
# ]

grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]

def add_zeros(grid):
    temp = [['0' for _ in range(len(grid[0])+2)]]
    for i in range(len(grid)):
        temp.append(['0'] + grid[i] + ['0'])
    temp.append(['0' for _ in range(len(grid[0])+2)])    
    return temp

def neighbours(row, col, grid):
    # print(grid[row][col], row, col)
    if( grid[row][col] == '1'):
        n = Node()
        if grid[row][col+1] == '1':
            n.right = neighbours(row, col+1, grid)
        if grid[row+1][col] == '1':
            n.bottom = neighbours(row+1, col, grid)
        return n

def numIslands(grid):
    n = []
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if grid[row][col] == '1' and grid[row][col-1] == '0' and grid[row-1][col] == '0':
                tmp = neighbours(row, col, grid)
                if tmp is not None:
                    n.append(tmp)
    print(n)
    return len(n)


            


print( numIslands(add_zeros(grid)) )
