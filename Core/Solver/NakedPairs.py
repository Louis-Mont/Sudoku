from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, tryremove, rm_coll


class NakedPairs(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Naked Pairs", sudoku)

    def solve(self):
        sudoku = self.sudoku
        for x, r in enumerate(sudoku.base):
            for y, c in enumerate(r):
                if sudoku.base[x, y] == 0:
                    dict_fp = {
                        self.h_pair: self.rm_h_pair,
                        self.v_pair: self.rm_v_pair,
                        self.sq_pair: self.rm_sq_pair
                    }
                    for k, v in dict_fp.items():
                        # False positive error
                        p = k(x, y)
                        if p:
                            v(p)

    def h_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and len(self.sudoku.sols[xb, y]) == 2 and self.sudoku.sols[xb, y] == self.sudoku.sols[xb, yb]:
                return xb, y
        return False

    def v_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and len(self.sudoku.sols[x, yb]) == 2 and self.sudoku.sols[x, yb] == self.sudoku.sols[xb, yb]:
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
                ls = len(self.sudoku.sols[ax, ay])
                if xb != ax or yb != ay and ls == 2 and self.sudoku.sols[ax, ay] == self.sudoku.sols[xb, yb]:
                    return ax, ay
        return False

    def rm_h_pair(self, xb, yb):
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y:
                rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[xb, y])

    def rm_v_pair(self, xb, yb):
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x:
                rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[x, yb])

    def rm_sq_pair(self, xb, yb):
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            for y, c in enumerate(r):
                if xb != x0 + x or yb != y0 + y and self.sudoku.base[x0 + x, y0 + y] == 0:
                    rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[x0 + x, y0 + y])
