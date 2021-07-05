from unittest import TestCase
import numpy as np
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.NakedPairs import NakedPairs
from Core.Solver.NakedTriples import NakedTriples
from Core.Solver.SudokuSolver import master_solver
from Core.Sudoku import Sudoku


class TestNakedTriples(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestNakedTriples, self).__init__(*args, **kwargs)
        ex1 = [[0, 7, 0, 4, 0, 8, 0, 2, 9],
               [0, 0, 2, 0, 0, 0, 0, 0, 4],
               [8, 5, 4, 0, 2, 0, 0, 0, 7],
               [0, 0, 8, 3, 7, 4, 2, 0, 0],
               [0, 2, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 3, 2, 6, 1, 7, 0, 0],
               [0, 0, 0, 0, 9, 3, 6, 1, 2],
               [2, 0, 0, 0, 0, 0, 4, 0, 3],
               [1, 3, 0, 6, 4, 2, 0, 7, 0]]
        self.ex1 = np.array(ex1)

        self.solvers = [NakedSingle, HiddenSingle, NakedPairs, NakedTriples]

    def test_Solve(self):
        sdk = Sudoku(self.ex1)
        NakedSingle(sdk).solve()

        sol = sdk.sols.copy()

        master_solver(self.solvers, sdk)

        self.assertNotEqual(sol, sdk.sols)
        self.assertEqual({4, 6, 7}, sdk.sols[4, 0])
        self.assertEqual({5, 8, 9}, sdk.sols[4, 3])
        self.assertEqual({5, 9}, sdk.sols[4, 5])
        self.assertEqual({1, 3}, sdk.sols[4, 6])
        self.assertEqual({4, 3}, sdk.sols[4, 7])
