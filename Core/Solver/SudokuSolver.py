from abc import ABC, abstractmethod
from Core.Sudoku import Sudoku


class SudokuSolver(ABC):
    def __init__(self, name):
        self.name = name
        self.sudoku = None

    @abstractmethod
    def solve(self, sudoku):
        pass
