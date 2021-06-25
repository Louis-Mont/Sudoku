from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, tryremove


class HiddenSingle(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Hidden Single", sudoku)

    def solve(self):
        sudoku = self.sudoku
        for x, r in enumerate(sudoku.base):
            for y in range(len(r)):
                if sudoku.base[x, y] == 0:
                    s = self.h_poss(x).union(self.v_poss(y)).union(self.sq_poss(x, y))
                    if len(s) == 1:
                        sudoku.base[x, y] = list(s)[0]

    def h_poss(self, x):
        all_poss = set(range(1, 10))
        for y, c in enumerate(self.sudoku.base[x]):
            self.rm_poss(x, y, all_poss)
        return all_poss

    def v_poss(self, y):
        all_poss = set(range(1, 10))
        for x, r in enumerate(self.sudoku.base[:, y]):
            self.rm_poss(x, y, all_poss)
        return all_poss

    def sq_poss(self, x, y):
        all_poss = set(range(1, 10))
        x0 = sq_o(x)
        y0 = sq_o(y)
        for r, sq_x in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            for c, sq_y in enumerate(sq_x):
                self.rm_poss(x0 + r, y0 + c, all_poss)
        return all_poss

    def rm_poss(self, x, y, lp):
        try:
            for s in self.sudoku.sols[x, y]:
                tryremove(lp, s)
        except KeyError:
            tryremove(lp, self.sudoku.base[x, y])
        return lp
