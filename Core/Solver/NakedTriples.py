from Core.Solver.SudokuSolver import SudokuSolver


class NakedTriples(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Naked Triples", sudoku)

    def _solve(self, x, y):
        pass
