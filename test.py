import sys
import sudokuSolver

"""
  Main function

  Executes testdata
"""
def main():
  sudokus = [
    [8, 9, 0, 1, 0, 4, 0, 2, 0],
    [0, 0, 1, 0, 6, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 9, 5, 1],
    [0, 0, 0, 8, 9, 0, 3, 4, 0],
    [3, 0, 0, 7, 0, 0, 1, 0, 0],
    [0, 5, 8, 0, 3, 6, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 5, 0, 4],
    [6, 0, 7, 5, 0, 0, 0, 0, 0],
    [4, 8, 0, 0, 0, 9, 0, 3, 6],
  ], [
    [0, 8, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 9, 0, 0, 0],
    [8, 0, 5, 0, 4, 0, 0, 0, 7],
    [0, 0, 0, 0, 3, 1, 0, 0, 4],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [3, 2, 0, 0, 8, 0, 1, 5, 0],
  ], [
    [6, 0, 0, 8, 5, 0, 9, 3, 1],
    [3, 5, 8, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 8, 3, 9, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 8, 3, 0, 6, 0, 1, 0, 0],
    [8, 3, 0, 0, 9, 0, 0, 0, 0],
    [0, 6, 0, 0, 8, 0, 2, 1, 9],
    [1, 0, 9, 0, 0, 5, 0, 0, 3],
  ], [
    [0, 0, 7, 0, 1, 3, 0, 0, 6],
    [0, 2, 0, 0, 9, 0, 0, 7, 0],
    [0, 3, 0, 8, 0, 0, 0, 0, 9],
    [0, 4, 3, 1, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 4, 3, 5, 0],
    [0, 0, 0, 0, 0, 1, 0, 9, 0],
    [0, 1, 0, 0, 7, 0, 0, 8, 0],
    [5, 0, 0, 6, 4, 0, 7, 0, 0],
  ]

  expected = [
    [8, 9, 3, 1, 5, 4, 6, 2, 7],
    [5, 2, 1, 9, 6, 7, 4, 8, 3],
    [7, 6, 4, 3, 8, 2, 9, 5, 1],
    [2, 7, 6, 8, 9, 1, 3, 4, 5],
    [3, 4, 9, 7, 2, 5, 1, 6, 8],
    [1, 5, 8, 4, 3, 6, 2, 7, 9],
    [9, 3, 2, 6, 7, 8, 5, 1, 4],
    [6, 1, 7, 5, 4, 3, 8, 9, 2],
    [4, 8, 5, 2, 1, 9, 7, 3, 6],
  ], [
    [7, 8, 2, 3, 1, 5, 4, 9, 6],
    [5, 3, 9, 6, 7, 4, 8, 1, 2],
    [1, 6, 4, 8, 2, 9, 3, 7, 5],
    [8, 1, 5, 9, 4, 2, 6, 3, 7],
    [2, 9, 6, 7, 3, 1, 5, 8, 4],
    [4, 7, 3, 5, 6, 8, 9, 2, 1],
    [9, 4, 1, 2, 5, 3, 7, 6, 8],
    [6, 5, 8, 1, 9, 7, 2, 4, 3],
    [3, 2, 7, 4, 8, 6, 1, 5, 9],
  ], [
    [6, 4, 2, 8, 5, 7, 9, 3, 1],
    [3, 5, 8, 9, 2, 1, 4, 6, 7],
    [7, 9, 1, 4, 3, 6, 8, 5, 2],
    [2, 7, 6, 5, 1, 8, 3, 9, 4],
    [4, 1, 5, 3, 7, 9, 6, 2, 8],
    [9, 8, 3, 2, 6, 4, 1, 7, 5],
    [8, 3, 7, 1, 9, 2, 5, 4, 6],
    [5, 6, 4, 7, 8, 3, 2, 1, 9],
    [1, 2, 9, 6, 4, 5, 7, 8, 3],
  ], [
    [9, 5, 7, 4, 1, 3, 8, 2, 6],
    [4, 2, 8, 5, 9, 6, 1, 7, 3],
    [6, 3, 1, 8, 2, 7, 5, 4, 9],
    [7, 4, 3, 1, 5, 8, 9, 6, 2],
    [8, 6, 5, 2, 3, 9, 4, 1, 7],
    [1, 9, 2, 7, 6, 4, 3, 5, 8],
    [2, 7, 4, 3, 8, 1, 6, 9, 2],
    [3, 1, 6, 9, 7, 5, 2, 8, 4],
    [5, 8, 9, 6, 4, 2, 7, 3, 1],
  ]

  for x, sudoku in enumerate(sudokus):
    solve = solveSudoku(sudoku)
    compareSudoku(expected[x], solve)

"""
  Solves a sudoku while displaying some basic debug data
"""
def solveSudoku(sudoku):
  outputSudoku(sudoku)
  grid = sudokuSolver.SudokuSolver()
  grid.setSudoku(sudoku)
  grid.solve()
  print
  outputSudoku(grid.getSudoku())
  print
  print str(grid.sudoku)
  print str(grid.isSolved())
  print
  print '--------------------------------------------------------------------------------'
  print

  return grid.getSudoku()

"""
  Printing a 2d sudoku
"""
def outputSudoku(sudoku):
  for rows in sudoku:
    for columns in rows:
       sys.stdout.write(str(columns))
    print

"""
  Compares a sudoku against a given solution
"""
def compareSudoku(expected, result):
  for x, row in enumerate(expected):
    for y, cell in enumerate(row):
      if result[x][y] == 0:
        continue # not found
      if result[x][y] != cell:
        print str([x, y]) + " expected to be " + str(cell) + " but found " + str(result[x][y])

if __name__ == '__main__':
  main()