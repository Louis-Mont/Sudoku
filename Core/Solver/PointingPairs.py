import numpy as np
from numpy import ndarray
from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, tryremove, rm_coll

class PointingPairs(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Pointing Pairs", sudoku)

    def _solve(self, x, y):
        x0 = sq_o(x)
        y0 = sq_o(y)
        # PAIR HORIZONTALE
        h_res = self.h_pair(x, y)
        if len(h_res) > 0:
            # Suppr aligned value
            for val in h_res:
                for yb, c in enumerate(self.sudoku.base[x]):
                    if y0 != sq_o(yb):
                        try:
                            tryremove(self.sudoku.sols[x, yb], val)
                        except KeyError:
                            continue

        # PAIR VERTICALE
        v_res = self.v_pair(x, y)
        if len(v_res) > 0:
            # Suppr aligned value
            for val in v_res:
                for xb, r in enumerate(self.sudoku.base[:, y]):
                    if x0 != sq_o(xb):
                        try:
                            tryremove(self.sudoku.sols[xb, y], val)
                        except KeyError:
                            continue

    def h_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        c_sol = self.sudoku.sols[xb, yb].copy()
        # Same line/box
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                # Same line, different column
                if xb == ax and yb != ay:
                    self.valid_sol(c_sol, ax, ay, True)
                # Different line
                if xb != ax and self.valid_sol(c_sol, ax, ay, False):
                    if not len(c_sol) > 0:
                        return c_sol
        
        return c_sol

    def v_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        c_sol = self.sudoku.sols[xb, yb].copy()
        # Same line/box
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                # Different line, same column
                if xb != ax and yb == ay:
                    self.valid_sol(c_sol, ax, ay, True)
                # Different column
                if yb != ay and self.valid_sol(c_sol, ax, ay, False):
                    if not len(c_sol) > 0:
                        return c_sol
        
        return c_sol
    
    def valid_sol(self, c_sol, x, y, on_same):
        """
        Verifies if the case x, y have the same pair as the case c_sol sent
        :type c_sol: set
        :type x: int
        :type y: int
        :type on_same: bool
        """
        try:
            t1 = np.array(list(c_sol))
            t2 = np.array(list(self.sudoku.sols[x, y]))
            i_res = np.intersect1d(t1, t2)
            if not on_same:
                for val in i_res:
                    c_sol.remove(val)
            return len(i_res) > 0
                
        except KeyError:
            return False