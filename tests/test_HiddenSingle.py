from unittest import TestCase
import numpy as np
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.SudokuSolver import master_solver
from Core.Sudoku import Sudoku


class TestHiddenSingle(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ex1 = [[2, 0, 0, 0, 7, 0, 0, 3, 8],
               [0, 0, 0, 0, 0, 6, 0, 7, 0],
               [3, 0, 0, 0, 4, 0, 6, 0, 0],
               [0, 0, 8, 0, 2, 0, 7, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 6],
               [0, 0, 7, 0, 3, 0, 4, 0, 0],
               [0, 0, 4, 0, 8, 0, 0, 0, 9],
               [0, 6, 0, 4, 0, 0, 0, 0, 0],
               [9, 1, 0, 0, 6, 0, 0, 0, 2]]
        self.ex1 = np.array(ex1)

        self.solvers = [NakedSingle, HiddenSingle]

    def test_ex1(self):
        base = self.ex1.copy()
        master_solver(self.solvers, Sudoku(self.ex1))
        self.assertNotEqual(base.all(), self.ex1.all())
