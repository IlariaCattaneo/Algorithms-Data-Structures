def check_sudoku(grid):
    x = len(grid)
    y = x
    columnSum = [0]*x

    for i in range(x):
        count = 0
        for j in range (y):
            columnSum[i] += grid[i][j]
            count += grid[i][j]
        if count != 45:
            print("fucked")
            return False 
    
    for el in columnSum:
        if el != 45:
            print("fucked")
            return False 
    
    def calculate3x3(xoffset,yoffset):
        Sum3x3 = 0
        for x in range(3):   
            for y in range(3):
                Sum3x3 += grid[xoffset + x][y + yoffset]
        return Sum3x3 == 45

    for x in range(len(grid), 3):
        for y in range(len(grid), 3):
            if not calculate3x3(x,y):
                return False
    print("BELLO")
    return True


print(check_sudoku([[1,2,3,4,5,6,7,8,9],
                    [4,5,6,7,8,9,1,2,3],
                    [7,8,9,1,2,3,4,5,6],
                    [2,3,4,5,6,7,8,9,1],
                    [5,6,7,8,9,1,2,3,4],
                    [8,9,1,2,3,4,5,6,7],
                    [3,4,5,6,7,8,9,1,2],
                    [6,7,8,9,1,2,3,4,5],
                    [9,1,2,3,4,5,6,7,8]]))

print(check_sudoku([[1,2,3,4,5,6,7,8,9],
                    [4,5,6,7,8,9,1,2,3],
                    [7,8,9,1,2,3,4,5,6],
                    [2,3,4,5,6,7,8,9,1],
                    [5,6,7,8,9,1,2,3,4],
                    [8,9,1,2,3,4,5,6,7],
                    [3,4,5,6,7,8,9,1,2],
                    [6,7,8,9,1,2,3,4,5],
                    [9,1,2,3,7,5,6,7,8]]))