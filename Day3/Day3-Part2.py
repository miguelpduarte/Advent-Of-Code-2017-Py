#!/usr/bin/python3

def updateMatrix(mat, x, y):
    mat[x][y] = mat[x-1][y] + mat[x+1][y] + mat[x-1][y-1] + mat[x][y-1] + mat[x+1][y-1] + mat[x-1][y+1] + mat[x][y+1] + mat[x+1][y+1]

input = 289326

#Defining constants for size of matrix (might change depending on input)
MAT_HEIGHT = 13
MAT_WIDTH = 13

#Creating zero initialized matrix
matrix = [[0 for x in range(0, MAT_WIDTH)] for y in range(0, MAT_HEIGHT)]

#Starting values
x = MAT_HEIGHT // 2
y = MAT_WIDTH // 2
matrix[x][y] = 1 #Starting with 1 in the center
lvl = 0

found = False

while not found:
    lvl += 1
    x += 1

    updateMatrix(matrix, x, y)
    if(matrix[x][y] > input):
        print(matrix[x][y], "is bigger than the input.")
        found = True
        break

    #The actual level side size but minus 1 since we always use it -1
    lvl_side_size = (2*lvl + 1) - 1

    #We update the variables in each loop because we want to use the updated values afterwards

    #going up
    for i in range(0, lvl_side_size - 1):
        y += 1
        updateMatrix(matrix, x, y)
        if(matrix[x][y] > input):
            print(matrix[x][y], "is bigger than the input.")
            found = True
            break

    #Avoiding excess processing
    if found:
        break

    #going left (on top)
    for i in range(0, lvl_side_size):
        x -= 1
        updateMatrix(matrix, x, y)
        if(matrix[x][y] > input):
            print(matrix[x][y], "is bigger than the input.")
            found = True
            break

    #Avoiding excess processing
    if found:
        break

    #going down (on the right)
    for i in range(0, lvl_side_size):
        y -= 1
        updateMatrix(matrix, x, y) 
        if(matrix[x][y] > input):
            print(matrix[x][y], "is bigger than the input.")
            found = True
            break

    #Avoiding excess processing
    if found:
        break

    #going right (on the bottom)
    for i in range(0, lvl_side_size):
        x += 1
        updateMatrix(matrix, x, y) 
        if(matrix[x][y] > input):
            print(matrix[x][y], "is bigger than the input.")
            found = True
            break


for line in matrix:
    for val in line:
        print(val, end='\t')
    print()
