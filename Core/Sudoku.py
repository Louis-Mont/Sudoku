import numpy as np
from numpy import ndarray
import random
from Core.Solver.NakedSingle import NakedSingle


class Sudoku:

    def __init__(self, base):
        """
        :param base: np 2d-array
        :type base: ndarray
        """
        self.base = base
        self.sols = {}

    def generate_complete_sudoku(self):
        x = 0
        while x < len(self.base):
            for y in range(len(self.base[x])):
                try:
                    ns = NakedSingle("ns")
                    ns.sudoku = self
                    c_sol = ns.get_sol(x, y)
                    pos = random.randint(0, len(c_sol) - 1)
                    self.base[x, y] = list(c_sol)[pos]
                except ValueError:
                    self.base[x] = [0 for i in range(9)]
                    x -= 1
                    break
            x += 1

    def drill_sudoku(self, c):
        i = 0
        while i < c:
            x = random.randint(0, len(self.base) - 1)
            y = random.randint(0, len(self.base[x]) - 1)
            if self.base[x, y] > 0:
                self.base[x, y] = 0
                i += 1
