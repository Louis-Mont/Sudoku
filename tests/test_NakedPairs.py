from unittest import TestCase
import numpy as np
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.NakedPairs import NakedPairs
from Core.Solver.SudokuSolver import master_solver
from Core.Sudoku import Sudoku


class TestNakedPairs(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestNakedPairs, self).__init__(*args, **kwargs)
        ex1 = [[4, 0, 0, 0, 0, 0, 9, 3, 8],
                [0, 3, 2, 0, 9, 4, 1, 0, 0],
                [0, 9, 5, 3, 0, 0, 2, 4, 0],
                [3, 7, 0, 6, 0, 9, 0, 0, 4],
                [5, 2, 9, 0, 0, 1, 6, 7, 3],
                [6, 0, 4, 7, 0, 3, 0, 9, 0],
                [9, 5, 7, 0, 0, 8, 3, 0, 0],
                [0, 0, 3, 9, 0, 0, 4, 0, 0],
                [2, 4, 0, 0, 3, 0, 7, 0, 9]]
        self.ex1 = np.array(ex1)

        self.solvers = [NakedSingle, HiddenSingle, NakedPairs]

    def test_solve(self):
        sdk = Sudoku(self.ex1)
        NakedSingle(sdk).solve()

        sol = sdk.sols.copy()
        base = sdk.base.copy()

        master_solver(self.solvers, sdk)

        self.assertNotEqual(sol, sdk.sols)
        self.assertEqual({2, 5}, sdk.sols[0, 3])
