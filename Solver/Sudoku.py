import numpy as np
from numpy import ndarray


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
