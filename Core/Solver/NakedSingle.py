from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import tryremove, sq_o


class NakedSingle(SudokuSolver):

    def __init__(self, sudoku):
        super().__init__("Naked Single", sudoku)

    def solve(self):
        sudoku = self.sudoku
        for x, r in enumerate(sudoku.base):
            for y, c in enumerate(r):
                if sudoku.base[x, y] == 0:
                    sudoku.sols[x, y] = self.get_sol(x, y)

    def h_sols(self, x):
        all_sol = self.get_poss()
        for y in self.sudoku.base[x]:
            tryremove(all_sol, y)
        return all_sol

    def v_sols(self, y):
        all_sol = self.get_poss()
        for x in self.sudoku.base[:, y]:
            tryremove(all_sol, x)
        return all_sol

    def sq_sol(self, x, y):
        all_sol = self.get_poss()
        for sq_x in self.sudoku.base[sq_o(x):sq_o(x) + 3, sq_o(y): sq_o(y) + 3]:
            for sq_y in sq_x:
                tryremove(all_sol, sq_y)
        return all_sol

    def get_sol(self, x, y):
        return self.h_sols(x).union(self.v_sols(y)).union(self.sq_sol(x, y))
