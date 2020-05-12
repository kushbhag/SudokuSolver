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

def initialize_assignment(theAssignment, board):
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            if board[row][col] == 0:
                theAssignment[(row, col)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                theAssignment[(row, col)] = [board[row][col]]

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

neighbors = dict()

def revise (theAssignment, x, y):
    revised = False
    theDomain = deepcopy(theAssignment[x])
    if len(theAssignment[y]) == 1:
        for arc in theAssignment[y]:
            if arc in theDomain:
                theAssignment[x].remove(arc)
                return True
    return revised

def ac3(theAssignment, arcs):
    while not len(arcs) == 0:
        constraint = arcs.pop(0)

        if revise(theAssignment, constraint[0], constraint[1]):
            if len(theAssignment[constraint[0]]) == 0:
                return False
            for n in neighbors[(constraint[0][0], constraint[0][1])]:
                if not (n, constraint[0]) in arcs:
                    arcs.append((n, constraint[0]))

def arc_consistency(theAssignment, board):
    arc = []
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            if not board[row][col] == 0:
                for n in neighbors[(row, col)]:
                    arc.append((n, (row, col)))
    ac3(theAssignment, arc)

def inferences(theAssignment, row, col):
    arcs = []
    for n in neighbors[(row, col)]:
        arcs.append((n, (row, col)))
    ac3(theAssignment, arcs)

def solve(theAssignment, board):
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            num = board[row][col]
            if num == 0:
                for i in theAssignment[(row, col)]:
                    if isConsistent(board, i, row, col):
                        board[row][col] = i
                        didSolve = solve(theAssignment, board)
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

def testBoard(board, name, tests):
    total_time = 0
    total_solve_time = 0
    print(name)
    for i in range(tests):
        assignment = dict()
        theBoard = deepcopy(board)
        initialize_assignment(assignment, theBoard)

        board_time = time.time()
        ac3_time = time.time()
        arc_consistency(assignment, theBoard)
        ac3_time = time.time() - ac3_time

        solve_time = time.time()
        solve(assignment, theBoard)
        solve_time = time.time() - solve_time
        board_time = time.time() - board_time


        #print("AC3 Time: %s" %round(ac3_time, 10), "Solving Time: %f" %round(solve_time, 10), "Execution took: %s " %board_time)
        total_solve_time += solve_time
        total_time += board_time
        print(theBoard)
    print ("Average Solve: %f" %(total_solve_time/tests))
    print ("Average Total: %f" %(total_time/tests))


initialize_neighbors(neighbors)
testBoard(board1, "BOARD 1", 20)
testBoard(board2, "BOARD 2", 20)
testBoard(board3, "BOARD 3", 2)
testBoard(board4, "BOARD 4", 20)
testBoard(board5, "BOARD 5", 5)
testBoard(board6, "BOARD 6", 20)
testBoard(board7, "BOARD 7", 20)
"""
board_time2 = testBoard(board2, "BOARD 2")
board_time3 = testBoard(board3, "BOARD 3")
board_time4 = testBoard(board4, "BOARD 4")
board_time5 = testBoard(board5, "BOARD 5")
board_time6 = testBoard(board6, "BOARD 6")
board_time7 = testBoard(board7, "BOARD 7")
"""