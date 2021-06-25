import numpy as np
import random
from Core.Sudoku import Sudoku
from Core.Solver.NakedSingle import NakedSingle

if __name__ == '__main__':
    grid = [[0 for i in range(9)] for j in range(0, 9)]

    arr = np.array(grid)
    sdk = Sudoku(arr)

    sdk.generate_complete_sudoku()
    # print(sdk.base)

    sdk.drill_sudoku(40)
    print(sdk.base)
    print()
    ns = NakedSingle(sdk)
    ns.solve()
    print(sdk.base)
