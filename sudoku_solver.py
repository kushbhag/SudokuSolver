import numpy as np
import time
from copy import deepcopy

ROW_SIZE = 9
COL_SIZE = 9
SQUARE_SIZE = 3

def inRow(board, num, row):
    if num in board[row]:
        return True
    return False

def inCol(board, num, col):
    if num in board[:,col]:
        return True
    return False

def inSquare(board, num, row, col):
    tempRow = (row // 3) * 3
    tempCol = (col // 3) * 3
    for i in range(SQUARE_SIZE):
        for j in range(SQUARE_SIZE):
            if board[tempRow][tempCol] == num:
                return True
            tempRow += 1
        tempCol += 1
        tempRow = (row // 3) * 3
    return False

def isConsistent(board, num, row, col):
    inTheRow = inRow(board, num, row)
    inTheCol = inCol(board, num, col)
    inTheSquare = inSquare(board, num, row, col)
    if not (inTheRow or inTheCol or inTheSquare):
        return True
    return False

def initialize_assignment(board, dict):
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            if board[row][col] == 0:
                dict[(row, col)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                dict[(row, col)] = [board[row][col]]

def initialize_neighbors(dict):
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            dict[(row, col)] = []
            for i in range(0, 9):
                if not (i, col) == (row, col):
                    dict[(row, col)].append((i, col))
                if not (row, i) == (row, col):
                    dict[(row, col)].append((row, i))
            tempRow = (row // 3) * 3
            tempCol = (col // 3) * 3
            for i in range(SQUARE_SIZE):
                for j in range(SQUARE_SIZE):
                    if not (tempRow, tempCol) == (row, col) and not (tempRow, tempCol) in dict[(row, col)]:
                        dict[(row, col)].append((tempRow, tempCol))
                    tempRow += 1
                tempCol += 1
                tempRow = (row // 3) * 3

def removeFromNeighbor(row, col, number):
    for n in neighbors[(row, col)]:
        if number in assignment[n] and not len(assignment[n]) == 1:
            assignment[n].remove(number)

def solveJustBacktracking(board, dict):
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            num = board[row][col]
            if num == 0:
                for i in dict[(row, col)]:
                    if isConsistent(board, i, row, col):
                        board[row][col] = i
                        didSolve = solveJustBacktracking(board, assignment)
                        if didSolve:
                            return True
                        else:
                            board[row][col] = num
                return False
    return True

board = np.array([
    [0,0,0,6,0,0,4,0,0],
    [7,0,0,0,0,3,6,0,0],
    [0,0,0,0,9,1,0,8,0],
    [0,0,0,0,0,0,0,0,0],
    [0,5,0,1,8,0,0,0,3],
    [0,0,0,3,0,6,0,4,5],
    [0,4,0,2,0,0,0,6,0],
    [9,0,3,0,0,0,0,0,0],
    [0,2,0,0,0,0,1,0,0],
])
assignment = dict()
neighbors = dict()
start = time.time()
initialize_assignment(board, assignment)
initialize_neighbors(neighbors)
for row in range(ROW_SIZE):
    for col in range(COL_SIZE):
        if not board[row][col] == 0:
            removeFromNeighbor(row, col, board[row][col])
solveJustBacktracking(board, assignment)
print (board)
print ("Amount of Time: %s" %(time.time() - start))
