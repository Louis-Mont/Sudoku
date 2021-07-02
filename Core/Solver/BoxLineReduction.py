import numpy as np
from numpy import ndarray
from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, tryremove, rm_coll

class BoxLineReduction(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Box Line Reduction", sudoku)

    def _solve(self, x, y):
        x0 = sq_o(x)
        y0 = sq_o(y)
        # BOX HORIZONTALE
        sq_h_res = self.sq_h_pair(x,y)
        if len(sq_h_res) > 0:
            # Suppr aligned value
            for val in sq_h_res:
                for xb, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
                    ax = x0 + xb
                    for yb, c in enumerate(r):
                        ay = y0 + yb
                        if x != ax:
                            try:
                                tryremove(self.sudoku.sols[ax, ay], val)
                            except KeyError:
                                continue

        # BOX VERTICALE
        sq_v_res = self.sq_v_pair(x,y)
        if len(sq_v_res) > 0:
            # Suppr aligned value
            for val in sq_v_res:
                for xb, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
                    ax = x0 + xb
                    for yb, c in enumerate(r):
                        ay = y0 + yb
                        if y != ay:
                            try:
                                tryremove(self.sudoku.sols[ax, ay], val)
                            except KeyError:
                                continue

    def sq_h_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        y0 = sq_o(yb)
        c_sol = self.sudoku.sols[xb, yb].copy()
        # Same line/box
        i = 0
        while i < len(c_sol):
            val = list(c_sol)[i]
            a_found = False
            for y, c in enumerate(self.sudoku.base[xb]):
                if y0 != sq_o(y) and self.contains_sol(xb, y, val):
                    a_found = True
            if a_found:
                tryremove(c_sol, val)
                i -= 1
            i += 1

        return c_sol

    def sq_v_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        x0 = sq_o(xb)
        c_sol = self.sudoku.sols[xb, yb].copy()
        # Same line/box
        i = 0
        while i < len(c_sol):
            val = list(c_sol)[i]
            a_found = False
            for x, r in enumerate(self.sudoku.base[:, yb]):
                if x0 != sq_o(x) and self.contains_sol(x, yb, val):
                    a_found = True
            if a_found:
                tryremove(c_sol, val)
                i -= 1
            i += 1

        return c_sol

    def contains_sol(self, x, y, val):
        """
        Verifies if the case x, y have the same value
        :type x: int
        :type y: int
        :type val: int
        """
        try:
            return list(self.sudoku.sols[x, y]).count(val) > 0
                
        except KeyError:
            return False