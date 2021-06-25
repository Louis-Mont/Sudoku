import numpy as np
import random
from Solver.Sudoku import Sudoku

if __name__ == '__main__':
    grid = [[0 for i in range(9)] for j in range(0, 9)]

    arr = np.array(grid)
    sdk = Sudoku(arr)

    sdk.generateCompleteSudoku()
    #print(sdk.base)

    sdk.drillSudoku(40)
    print(sdk.base)

    
