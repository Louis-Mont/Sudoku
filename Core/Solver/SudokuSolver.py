from abc import ABC, abstractmethod


class SudokuSolver(ABC):
    def __init__(self, name, sudoku=None):
        self.name = name
        self.sudoku = sudoku

    def get_poss(self):
        return set(range(1, 10))

    @abstractmethod
    def solve(self):
        pass
