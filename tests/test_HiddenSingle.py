from unittest import TestCase
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.NakedSingle import NakedSingle


class TestHiddenSingle(TestCase):
    def __init__(self):
        super().__init__()
        self.ex1 = [[2, 0, 0, 0, 7, 0, 0, 3, 8],
                    [0, 0, 0, 0, 0, 6, 0, 7, 0],
                    [3, 0, 0, 0, 4, 0, 6, 0, 0],
                    [0, 0, 8, 0, 2, 0, 7, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 6],
                    [0, 0, 7, 0, 3, 0, 4, 0, 0],
                    [0, 0, 4, 0, 8, 0, 0, 0, 9],
                    [0, 6, 0, 4, 0, 0, 0, 0, 0],
                    [9, 1, 0, 0, 6, 0, 0, 0, 2]]

        self.solvers = [NakedSingle, HiddenSingle]

    def test_solve(self):
        pass
