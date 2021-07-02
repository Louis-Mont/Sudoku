from unittest import TestCase
import numpy as np
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.BoxLineReduction import BoxLineReduction
from Core.Solver.SudokuSolver import master_solver
from Core.Sudoku import Sudoku

class TestBoxLineReduction(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBoxLineReduction, self).__init__(*args, **kwargs)

        self.solvers = [NakedSingle, HiddenSingle, BoxLineReduction]

    def test_solve(self):
        sdk = Sudoku(np.zeros((9, 9)))
        sdk.formating_sudoku("020943715904000600750000040500480000200000453400352000042000081005004260090208504")
        NakedSingle(sdk).solve()

        sol = sdk.sols.copy()

        sdk.print_sudoku()

        master_solver(self.solvers, sdk)

        self.assertNotEqual(sol, sdk.sols)
        self.assertEqual({1, 3, 7, 9}, sdk.sols[3, 2])
        self.assertEqual({7, 8}, sdk.sols[7, 1])
