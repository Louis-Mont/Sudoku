from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, rm_coll


class NakedTriples(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Naked Triples", sudoku)

    def _solve(self, x, y):
        if 2 <= len(self.sudoku.sols[x, y]) <= 3:
            pass

    def h_triple(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        triple_candidate = ()
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.valid_sol(xb, yb, xb, y):
                if self.valid_triple((xb, yb), (xb, y), triple_candidate):
                    return {(xb, yb), (xb, y), triple_candidate}
                else:
                    triple_candidate = xb, y
        return False

    def v_triple(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        triple_candidate = ()
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and self.valid_sol(xb, yb, x, yb):
                if self.valid_triple((xb, yb), (x, yb), triple_candidate):
                    return {(xb, yb), (x, yb), triple_candidate}
                else:
                    triple_candidate = x, yb
        return False

    def sq_triple(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        triple_candidate = ()
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                if (xb != ax or yb != ay) and self.valid_sol(xb, yb, ax, ay):
                    if self.valid_triple((xb, yb), (ax, ay), triple_candidate):
                        return {(xb, yb), (ax, ay), triple_candidate}
                    else:
                        triple_candidate = ax, ay
        return False

    def rm_h_triple(self, xb, yb):
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.not_triple(xb, yb, xb, y):
                rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[xb, y])

    def rm_v_triple(self, xb, yb):
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.not_triple(xb, yb, xb, y):
                rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[xb, y])

    def rm_sq_triple(self, xb, yb):
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and self.not_triple(xb, yb, x, yb):
                rm_coll(self.sudoku.sols[xb, yb], self.sudoku.sols[x, yb])

    def valid_sol(self, xb, yb, x, y):
        sols = self.sudoku.sols
        try:
            return len(sols[xb, yb] - sols[x, y]) <= 1 and sols[xb, yb] != sols[x, y]
        except KeyError:
            return False

    def valid_triple(self, first, second, third):
        xb, yb = first
        x, y = second
        xt, yt = third
        try:
            return self.valid_sol(xb, yb, xt, yt) and self.valid_sol(x, y, xt, yt)
        except KeyError:
            return False

    def not_triple(self, xb, yb, x, y):
        try:
            return self.sudoku.sols[xb, yb].issuperset(self.sudoku.sols[x, y])
        except KeyError:
            return False
