import numpy as np
import random
from Solver.Sudoku import Sudoku

if __name__ == '__main__':
    p = [random.sample(range(10), 9) for j in range(0, 9)]
    # print(p)
    arr = np.array(p)
    print(arr)
    sv = Sudoku(arr)
    sv.solve()
    print(sv.base)
