from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, tryremove, rm_coll


class NakedPairs(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Naked Pairs", sudoku)

    def _solve(self, x, y):
        pairs = [
            (self.h_pair(x, y), self.rm_h_pair),
            (self.v_pair(x, y), self.rm_v_pair),
            (self.sq_pair(x, y), self.rm_sq_pair)
        ]
        for pair_v in pairs:
            pair = pair_v[0]
            # False positive error
            if pair:
                pair_v[1](pair[0], pair[1])

    def h_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.valid_sol(xb, yb, xb, y):
                return xb, y
        return False

    def v_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and self.valid_sol(xb, yb, x, yb):
                return x, yb
        return False

    def sq_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                if (xb != ax or yb != ay) and self.valid_sol(xb, yb, ax, ay):
                    return ax, ay
        return False

    def rm_h_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.not_pair(xb, yb, xb, y):
                rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[xb, y])

    def rm_v_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and self.not_pair(xb, yb, x, yb):
                rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[x, yb])

    def rm_sq_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                if (xb != ax or yb != ay) and self.not_pair(xb, yb, ax, ay):
                    rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[ax, ay])

    def valid_sol(self, xb, yb, x, y):
        """
        Verifies if the case x, y have the same pair as xb, yb
        :type xb: int
        :type yb: int
        :type x: int
        :type y: int
        """
        try:
            return len(self.sudoku.sols[x, y]) == 2 and self.sudoku.sols[x, y] == self.sudoku.sols[xb, yb]
        except KeyError:
            return False

    def not_pair(self, xb, yb, x, y):
        """
        Verifies if the case x, y is not the same pair as xb, yb but still have a sol
        :type xb: int
        :type yb: int
        :type x: int
        :type y: int
        """
        try:
            return self.sudoku.base[x, y] == 0 and self.sudoku.sols[x, y] != self.sudoku.sols[xb, yb]
        except KeyError:
            return False
