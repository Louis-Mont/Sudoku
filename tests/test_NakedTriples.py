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

        ex2 = [[2, 9, 4, 5, 1, 3, 0, 0, 6],
               [6, 0, 0, 8, 4, 2, 3, 1, 9],
               [3, 0, 0, 6, 9, 7, 2, 5, 4],
               [0, 0, 0, 0, 5, 6, 0, 0, 0],
               [0, 4, 0, 0, 8, 0, 0, 6, 0],
               [0, 0, 0, 4, 7, 0, 0, 0, 0],
               [7, 3, 0, 1, 6, 4, 0, 0, 5],
               [9, 0, 0, 7, 3, 5, 0, 0, 1],
               [4, 0, 0, 9, 2, 8, 6, 3, 7]]

        self.ex2 = np.array(ex2)

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
        self.assertEqual({1, 3}, sdk.sols[4, 6])  # Hidden Singles does not removes the 1
        self.assertEqual({4, 3, 6}, sdk.sols[4, 7])

    def test_Solve2(self):
        sdk = Sudoku(self.ex2)
        NakedSingle(sdk).solve()
        sol = sdk.sols.copy()

        master_solver(self.solvers, sdk)

        self.assertNotEqual(sol, sdk.sols)
        self.assertEqual({2, 7}, sdk.sols[3, 1])
        self.assertEqual({2, 3, 7, 9}, sdk.sols[3, 2])
        self.assertEqual({1, 4, 7, 9}, sdk.sols[3, 6])
        self.assertEqual({2, 3, 6}, sdk.sols[5, 2])
        self.assertEqual({9}, sdk.sols[5, 7])
        self.assertEqual({1, 5, 9}, sdk.sols[5, 6])
        self.assertEqual({7, 8}, sdk.sols[0, 6])
