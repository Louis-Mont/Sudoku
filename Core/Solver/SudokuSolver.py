from abc import ABC, abstractmethod
from Core.utils import tryremove


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
        self.set_one_sol()

    def set_one_sol(self):
        for k, v in self.sudoku.sols.items():
            if len(v) == 1:
                self.sudoku.base[k] = list(v)[0]

    def get_poss(self):
        return set(range(1, 10))

    def rm_poss(self, x, y, lp):
        """
        Removes the possibilities comprised either in the case's solutions or in the case, if already filled
        :type x: int
        :type y: int
        :param lp: The possibilities left when you're calling the function
        :type lp: set[int]
        """
        try:
            for s in self.sudoku.sols[x, y]:
                tryremove(lp, s)
        except KeyError:
            tryremove(lp, self.sudoku.base[x, y])
        return lp

    @abstractmethod
    def solve(self):
        pass
