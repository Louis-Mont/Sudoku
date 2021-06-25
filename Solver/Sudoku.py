import numpy as np
from numpy import ndarray
import random

class Sudoku:

    def __init__(self, base):
        """
        :param base: np 2d-array
        :type base: ndarray
        """
        self.base = base
        self.sols = {}
        x = 0
        for r in base:
            for y in range(len(r)):
                s = self.h_sols(x).intersection(self.v_sols(y)).intersection(self.sq_sol(x, y))
                if len(s) == 1:
                    base[x, y] = list(s)[0]
                else:
                    self.sols[x, y] = s
            x += 1

    def h_sols(self, x):
        all_sol = {i for i in range(1, 10)}
        for y in self.base[x]:
            self.tryremove(all_sol, y)
        return all_sol

    def v_sols(self, y):
        all_sol = {i for i in range(1, 10)}
        for x in self.base[:, y]:
            self.tryremove(all_sol, x)
        return all_sol

    def sq_o(self, n):
        return (n // 3) * 3

    def sq_sol(self, x, y):
        all_sol = {i for i in range(1, 10)}
        for sq_x in self.base[self.sq_o(x):self.sq_o(x) + 3, self.sq_o(y): self.sq_o(y) + 3]:
            for sq_y in sq_x:
                self.tryremove(all_sol, sq_y)
        return all_sol

    def tryremove(self, l, v):
        try:
            l.remove(v)
        except ValueError:
            pass
        except KeyError:
            # TODO : Not Good Sudoku
            pass
        return l

    def generateCompleteSudoku(self):
        x = 0
        while x < len(self.base):
            for y in range(len(self.base[x])):
                try:
                    cSol = self.h_sols(x).intersection(self.v_sols(y)).intersection(self.sq_sol(x, y))
                    pos = random.randint(0, len(cSol) - 1)
                    self.base[x, y] = list(cSol)[pos]
                except:
                    self.base[x] = [0 for i in range(9)]
                    x -= 1
                    break
            x += 1

    def drillSudoku(self, c):
        i = 0
        while i < c:
            x = random.randint(0, len(self.base) - 1)
            y = random.randint(0, len(self.base[x]) - 1)
            if self.base[x,y] > 0:
                self.base[x,y] = 0
                i += 1
