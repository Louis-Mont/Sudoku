from abc import ABC, abstractmethod
from Core.utils import tryremove


def master_solver(solvers, sudoku):
    """
    Solve the sudoku, with all the solvers provided, non-instanced
    :type solvers: list[type[SudokuSolver]]
    :type sudoku: Sudoku
    """
    for solver in solvers:
        slv = solver(sudoku)
        slv.solve()
        slv.set_one_sol()


class SudokuSolver(ABC):
    def __init__(self, name, sudoku=None):
        self.name = name
        self.sudoku = sudoku

    def set_one_sol(self):
        for k, v in self.sudoku.sols.items():
            if len(v) == 1:
                self.sudoku.base[k] = list(v)[0]

    def get_poss(self):
        return set(range(1, 10))

    def solve(self):
        """
        Solves the sudoku using the current solver
        """
        sudoku = self.sudoku
        for x, r in enumerate(sudoku.base):
            for y, c in enumerate(r):
                if sudoku.base[x, y] == 0:
                    self._solve(x, y)

    @abstractmethod
    def _solve(self, x, y):
        """
        Called every time the function goes on a non resolved case when browsing the array
        :param x,y: coords of the current case being browsed
        :type x: int
        :type y: int
        """
        pass
