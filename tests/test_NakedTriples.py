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
        ex1 = [[]]
        self.ex1 = np.array(ex1)

        self.solvers = [NakedSingle, HiddenSingle, NakedPairs, NakedTriples]

    def test_Solve(self):
        sdk = Sudoku(self.ex1)
        NakedSingle(sdk).solve()

        sol = sdk.sols.copy()

        master_solver(self.solvers, sdk)
