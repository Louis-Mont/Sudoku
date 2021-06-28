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
                    for s in [self.h_poss(x, y), self.v_poss(x, y), self.sq_poss(x, y)]:
                        if len(s) == 1:
                            self.sudoku.sols[x, y] = s
                            break

    def h_poss(self, xb, yb):
        case_poss = self.sudoku.sols[xb, yb].copy()
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.sudoku.base[xb, y] == 0:
                case_poss -= self.sudoku.sols[xb, y]
        return case_poss

    def v_poss(self, xb, yb):
        case_poss = self.sudoku.sols[xb, yb].copy()
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and self.sudoku.base[x, yb] == 0:
                case_poss -= self.sudoku.sols[x, yb]
        return case_poss

    def sq_poss(self, xb, yb):
        case_poss = self.sudoku.sols[xb, yb].copy()
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            # real position of x in the global table
            ax = x0 + x
            for y, c in enumerate(r):
                # real position of y in the global table
                ay = y0 + y
                # parentheses to change priority of operations
                if (xb != ax or yb != ay) and self.sudoku.base[ax, ay] == 0:
                    case_poss -= self.sudoku.sols[ax, ay]
        return case_poss
