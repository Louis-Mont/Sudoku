from abc import ABC, abstractmethod


class SudokuSolver(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def solve(self):
        pass
