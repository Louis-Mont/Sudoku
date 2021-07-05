from unittest import TestCase
import numpy as np
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.PointingPairs import PointingPairs
from Core.Solver.SudokuSolver import master_solver
from Core.Sudoku import Sudoku

class TestPointingPairs(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPointingPairs, self).__init__(*args, **kwargs)

        self.solvers = [NakedSingle, HiddenSingle, PointingPairs]

    def test_solve(self):
        sdk = Sudoku(np.zeros((9, 9)))
        sdk.formating_sudoku("017903600000080000900000507072010430000402070064370250701000065000030000005601720")
        NakedSingle(sdk).solve()

        sol = sdk.sols.copy()

        sdk.print_sudoku()

        master_solver(self.solvers, sdk)

        self.assertNotEqual(sol, sdk.sols)
        self.assertEqual({2, 4, 5, 6}, sdk.sols[1, 0])