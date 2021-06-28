from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, tryremove


class NakedPairs(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Naked Pairs", sudoku)

    def solve(self):
        pass
