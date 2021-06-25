import numpy as np
from numpy import ndarray
import random

class Sudoku:

    def __init__(self, base):
        """
        :param base: np 2d-array
        :type base: ndarray
        """
        self.base = base
        self.sols = {}


    def generateCompleteSudoku(self):
        x = 0
        while x < len(self.base):
            for y in range(len(self.base[x])):
                try:
                    cSol = self.h_sols(x).intersection(self.v_sols(y)).intersection(self.sq_sol(x, y))
                    pos = random.randint(0, len(cSol) - 1)
                    self.base[x, y] = list(cSol)[pos]
                except:
                    self.base[x] = [0 for i in range(9)]
                    x -= 1
                    break
            x += 1

    def drillSudoku(self, c):
        i = 0
        while i < c:
            x = random.randint(0, len(self.base) - 1)
            y = random.randint(0, len(self.base[x]) - 1)
            if self.base[x,y] > 0:
                self.base[x,y] = 0
                i += 1
