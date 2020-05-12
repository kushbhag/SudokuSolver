"""
This program uses a simple backtracking algorithm tested on 5 sudoku puzzles
"""
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

def solveJustBacktracking(board):
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            num = board[row][col]
            if num == 0:
                for i in range(1,10):
                    if isConsistent(board, i, row, col):
                        board[row][col] = i
                        didSolve = solveJustBacktracking(board)
                        if didSolve:
                            return True
                        else:
                            board[row][col] = num
                return False
    return True

board1 = np.array([
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
])
board2 = np.array([
    [0,2,0,6,0,8,0,0,0],
    [5,8,0,0,0,9,7,0,0],
    [0,0,0,0,4,0,0,0,0],
    [3,7,0,0,0,0,5,0,0],
    [6,0,0,0,0,0,0,0,4],
    [0,0,8,0,0,0,0,1,3],
    [0,0,0,0,2,0,0,0,0],
    [0,0,9,8,0,0,0,3,6],
    [0,0,0,3,0,6,0,9,0]
])
board3 = np.array([
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
board4 = np.array([
    [2,0,0,3,0,0,0,0,0],
    [8,0,4,0,6,2,0,0,3],
    [0,1,3,8,0,0,2,0,0],
    [0,0,0,0,2,0,3,9,0],
    [5,0,7,0,0,0,6,2,1],
    [0,3,2,0,0,6,0,0,0],
    [0,2,0,0,0,9,1,4,0],
    [6,0,1,2,5,0,8,0,9],
    [0,0,0,0,0,1,0,0,2]
])
board5 = np.array([
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]
])
board6 = np.array([
    [5,0,0,0,0,1,0,0,0],
    [1,0,7,2,0,0,0,4,0],
    [0,8,0,5,0,0,2,1,9],
    [0,0,0,7,0,0,0,3,0],
    [0,0,8,0,1,0,6,0,0],
    [0,7,0,0,0,5,0,0,0],
    [7,5,9,0,0,2,0,6,0],
    [0,4,0,0,0,8,7,0,1],
    [0,0,0,6,0,0,0,0,3]
])
board7 = np.array([
    [0,0,5,0,9,0,0,0,0],
    [9,0,0,4,0,0,0,0,0],
    [0,7,0,0,0,0,5,0,1],
    [0,0,6,8,0,0,0,0,2],
    [1,0,8,0,0,0,3,0,7],
    [5,0,0,0,0,9,1,0,0],
    [6,0,3,0,0,0,0,4,0],
    [0,0,0,0,0,1,0,0,3],
    [0,0,0,0,8,0,6,0,0]
])

board_time1 = time.time()
solveJustBacktracking(board1)
print(board1)
board_time1 = time.time() - board_time1
print("Execution took: %s " % board_time1)

board_time2 = time.time()
solveJustBacktracking(board2)
print(board2)
board_time2 = time.time() - board_time2
print("Execution took: %s " % board_time2)

board_time3 = time.time()
solveJustBacktracking(board3)
print(board3)
board_time3 = time.time() - board_time3
print("Execution took: %s " % board_time3)

board_time4 = time.time()
solveJustBacktracking(board4)
print(board4)
board_time4 = time.time() - board_time4
print("Execution took: %s " % board_time4)

board_time5 = time.time()
solveJustBacktracking(board5)
print(board5)
board_time5 = time.time() - board_time5
print("Execution took: %s " % board_time5)

board_time6 = time.time()
solveJustBacktracking(board6)
print(board6)
board_time6 = time.time() - board_time6
print("Execution took: %s " % board_time6)

board_time7 = time.time()
solveJustBacktracking(board7)
print(board7)
board_time7 = time.time() - board_time7
print("Execution took: %s " % board_time7)
print("Total Time = %s " %(board_time1 + board_time2 + board_time3 + board_time4 + board_time5 + board_time6 + board_time7))
"""
Board 1 = 0.005984067916870117
Board 2 = 0.22541165351867676
Board 3 = 88.84742617607117
Board 4 = 0.44281554222106934
Board 5 = 7.832394123077393
Board 6 =
Board 7 = 
Totatl time = 97.35403156280518
"""

