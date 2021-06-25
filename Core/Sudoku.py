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
                    ns = NakedSingle(self)
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
        while i < c and not self.is_sudoku_empty():
            x = random.randint(0, len(self.base) - 1)
            y = random.randint(0, len(self.base[x]) - 1)
            if self.base[x, y] > 0:
                self.base[x, y] = 0
                i += 1

    def is_sudoku_empty(self):
        is_empty = True
        for x in range(0, len(self.base)):
            if not list(self.base[x]).count(0) == len(self.base[x]):
                is_empty = False

        return is_empty

    def is_sudoku_valid(self):
        is_valid = True
        for x in range(len(self.base)):
            for y in range(len(self.base[x])):
                ns = NakedSingle(self)
                val = self.base[x, y]
                self.base[x, y] = 0
                c_sol = ns.get_sol(x, y)
                if val != 0 and not (list(c_sol).count(val) > 0):
                    is_valid = False
                self.base[x, y] = val

        return is_valid

    def formating_sudoku(self, fc):
        x = 0
        y = 0
        for car in fc:
            if y == len(self.base[x]):
                y = 0
                x += 1
            try:
                c = int(car)
                if c >= 0 and c <= 9:
                    self.base[x,y] = c
                    y += 1
            except ValueError:
                if y != len(self.base[x]) and x != len(self.base) and not str(car) == "\n":
                    self.base[x,y] = 0
                    y += 1
                else:
                    continue
