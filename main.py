import numpy as np
import random
from Core.Sudoku import Sudoku
from Core.Solver.NakedSingle import NakedSingle

if __name__ == '__main__':
    grid = [[0 for i in range(9)] for j in range(0, 9)]

    arr = np.array(grid)
    sdk = Sudoku(arr)

    #
    sudoku_file = "908000605\n645793021\n000058000\n007130298\n039000010\n010070560\n350907006\n000310400\n490506072"
    sudoku_file2 = "9-8---6-5\n645793-21\n----58---\n--713-298\n-39----1-\n-1--7-56-\n35-9-7--6\n---31-4--\n49-5-6-72"
    sudoku_file3 = "9.8...6.5645793.21....58.....713.298.39....1..1..7.56.35.9.7..6...31.4..49.5.6.72"
    sdk.formating_sudoku(sudoku_file)
    #

    #sdk.generate_complete_sudoku()
    print(sdk.base)

    #sdk.drill_sudoku(40)
    #print(sdk.base)

    is_valid = sdk.is_sudoku_valid()
    print(is_valid)

    print()
    ns = NakedSingle(sdk)
    ns.solve()
    #print(sdk.base)
