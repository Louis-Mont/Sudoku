import numpy as np
from numpy import ndarray
from Core.utils import tryremove, sq_o


class Sudoku:

    def __init__(self, base):
        """
        :param base: np 2d-array
        :type base: ndarray
        """
        self.base = base
        self.sols = {}

    def h_sols(self, x):
        all_sol = set(range(1, 10))
        for y in self.base[x]:
            tryremove(all_sol, y)
        return all_sol

    def v_sols(self, y):
        all_sol = set(range(1, 10))
        for x in self.base[:, y]:
            tryremove(all_sol, x)
        return all_sol

    def sq_sols(self, x, y):
        all_sol = set(range(1, 10))
        for sq_x in self.base[sq_o(x):sq_o(x) + 3, sq_o(y): sq_o(y) + 3]:
            for sq_y in sq_x:
                tryremove(all_sol, sq_y)
        return all_sol

    def solve(self):
        solved = False
        while not solved:
            blanks = np.count_nonzero(self.base == 0)
            solved = True
            for x, r in enumerate(self.base):
                for y in range(len(r)):
                    if self.base[x, y] == 0:
                        solved = False
                        s = self.h_sols(x).intersection(self.v_sols(y)).intersection(self.sq_sols(x, y))
                        if len(s) == 1:
                            self.base[x, y] = list(s)[0]
                            try:
                                self.sols.pop((x, y))
                            except KeyError:
                                pass
                        else:
                            self.sols[x, y] = s
            if blanks == np.count_nonzero(self.base == 0):
                return
