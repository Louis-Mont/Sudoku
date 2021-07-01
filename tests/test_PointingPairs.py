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

        ex2 = [[0, 8, 0, 0, 9, 0, 0, 3, 0],
               [0, 3, 0, 0, 0, 0, 0, 6, 9],
               [9, 0, 2, 0, 6, 3, 1, 5, 8],
               [0, 1, 0, 8, 0, 4, 5, 9, 0],
               [8, 5, 1, 9, 0, 7, 0, 4, 6],
               [3, 9, 4, 6, 0, 5, 8, 7, 0],
               [5, 6, 3, 0, 4, 0, 9, 8, 7],
               [2, 0, 0, 0, 0, 0, 0, 1, 5],
               [0, 1, 0, 0, 5, 0, 0, 2, 0]]
        self.ex2 = np.array(ex2)

        self.solvers = [NakedSingle, HiddenSingle, PointingPairs]

    def test_solve(self):
        sdk = Sudoku(np.zeros((9, 9)))
        sdk.formating_sudoku("017903600000080000900000507072010430000402070064370250701000065000030000005601720")
        NakedSingle(sdk).solve()

        sol = sdk.sols.copy()

        sdk.print_sudoku()
        for x, r in enumerate(sdk.base):
            print("Ligne " + str(x) + " : ")
            for y, c in enumerate(r):
                try:
                    print("- " + str(y) + " > " + str(sol[x,y]))
                except KeyError:
                    print("- " + str(y) + " > " + str(sdk.base[x,y]))

        master_solver(self.solvers, sdk)

        """self.assertNotEqual(sol, sdk.sols)
        self.assertEqual({2, 5}, sdk.sols[0, 3])
        self.assertEqual({8}, sdk.sols[2, 0])
        self.assertEqual({2, 5}, sdk.sols[5, 4])
        self.assertEqual({5, 6, 7}, sdk.sols[1, 8])"""

    def test_solve2(self):
        sdk = Sudoku(self.ex2)
        NakedSingle(sdk).solve()

        sol = sdk.sols.copy()

        master_solver(self.solvers, sdk)

        """self.assertNotEqual(sol, sdk.sols)
        self.assertEqual({8, 9}, sdk.sols[7, 2])
        self.assertEqual({1, 2, 4, 5}, sdk.sols[0, 3])
        self.assertEqual({6, 8, 9}, sdk.sols[7, 5])
        self.assertEqual({6, 8, 9}, sdk.sols[8, 5])"""
