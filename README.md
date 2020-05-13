# SudokuSolver
Implementing multiple Sudoku solvers to test which one is the fastest.

1) bt_sudoku_solver: Uses a simple backtracking algorithm with no improvements at all
2) ac3_sudoku_solver: Uses an AC3 algorithm that removes any arcs between neighboring cells. This approach is meant to create arc consistency before the backtracking approach is run. In turn, this improves the solving speed of the program by up to 50%.
