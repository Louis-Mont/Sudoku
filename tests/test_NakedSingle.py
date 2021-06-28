from unittest import TestCase
import numpy as np
from Core.Sudoku import Sudoku
from Core.Solver.NakedSingle import NakedSingle


class TestNakedSingle(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestNakedSingle, self).__init__(*args, **kwargs)
        grid = Sudoku(np.zeros((9, 9)))
        grid.generate_complete_sudoku()
        grid.drill_sudoku(20)
        self.grid = grid

    def test_Solve(self):
        ns = NakedSingle(self.grid)
        ns.solve()
        ns.set_one_sol()
