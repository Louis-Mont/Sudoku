from abc import ABC, abstractmethod


class SudokuSolver(ABC):
    def __init__(self, name, sudoku=None):
        self.name = name
        self.sudoku = sudoku

    @abstractmethod
    def solve(self):
        pass
