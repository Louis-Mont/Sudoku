from abc import ABC, abstractmethod


class SudokuSolver(ABC):
    def __init__(self, name, sudoku=None):
        self.name = name
        self.sudoku = sudoku

    def master_solver(self, solvers):
        """
        Solve the sudoku, with all the solvers provided, non-instanced
        :type solvers: list[type[SudokuSolver]]
        """
        for solver in solvers:
            solver(self.sudoku).solve()
        for k, v in self.sudoku.sols:
            if len(v) == 1:
                self.sudoku.base[k] = list(v)[0]

    def get_poss(self):
        return set(range(1, 10))

    @abstractmethod
    def solve(self):
        pass
