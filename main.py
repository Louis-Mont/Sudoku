import numpy as np
import random
from Core.Sudoku import Sudoku
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.HiddenSingle import HiddenSingle

if __name__ == '__main__':
    exhs = [[2, 0, 0, 0, 7, 0, 0, 3, 8],
            [0, 0, 0, 0, 0, 6, 0, 7, 0],
            [3, 0, 0, 0, 4, 0, 6, 0, 0],
            [0, 0, 8, 0, 2, 0, 7, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 7, 0, 3, 0, 4, 0, 0],
            [0, 0, 4, 0, 8, 0, 0, 0, 9],
            [0, 6, 0, 4, 0, 0, 0, 0, 0],
            [9, 1, 0, 0, 6, 0, 0, 0, 2]]

    grid = [[0 for i in range(9)] for j in range(0, 9)]

    arr = np.array(exhs)
    sdk = Sudoku(arr)

    # sdk.generate_complete_sudoku()
    # print(sdk.base)

    # sdk.drill_sudoku(40)
    sdkbase = sdk.base.copy()
    print(sdkbase)
    print()
    ns = NakedSingle(sdk)
    ns.solve()
    sdkns = sdk.base
    print((sdkbase == sdkns).all())
    hs = HiddenSingle(sdk)
    hs.solve()
    print()
    print((sdkns == sdk.base).all())

    print(sdk.base)
