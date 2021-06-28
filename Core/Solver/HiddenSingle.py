from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, tryremove


class HiddenSingle(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Hidden Single", sudoku)

    def solve(self):
        sudoku = self.sudoku
        for x, r in enumerate(sudoku.base):
            for y, c in enumerate(r):
                if sudoku.base[x, y] == 0:
                    s = self.h_poss(x, y).union(self.v_poss(x, y)).union(self.sq_poss(x, y))
                    if len(s) == 1:
                        sudoku.base[x, y] = list(s)[0]

    def h_poss(self, xb, yb):
        all_poss = self.get_poss()
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y:
                self.rm_poss(xb, y, all_poss)
        return all_poss

    def v_poss(self, xb, yb):
        all_poss = self.get_poss()
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x:
                self.rm_poss(x, yb, all_poss)
        return all_poss

    def sq_poss(self, xb, yb):
        all_poss = self.get_poss()
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            for y, c in enumerate(r):
                if xb != x0 + x or yb != y0 + y:
                    self.rm_poss(x0 + x, y0 + y, all_poss)
        return all_poss
