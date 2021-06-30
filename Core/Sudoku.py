import numpy as np
from numpy import ndarray
import random
from Core.Solver.NakedSingle import NakedSingle

class Sudoku:

    def __init__(self, base):
        """
        :param base: np 2d-array
        :type base: ndarray
        """
        self.base = base
        self.sols: dict[tuple[int, int], set[int]] = {}

    def generate_sudoku(self, drill_rate=0.5):
        while not self.is_sudoku_complete():
            n = 9
            # Initialiser une grille vide
            self.base = np.zeros((n, n), np.int)
            # Tirage premiere ligne en random
            suite_nb = np.arange(1, n + 1)
            self.base[0, :] = np.random.choice(suite_nb, n, replace=False)
            try:
                # Parcourt par ligne
                for x in range(1, n):
                    # Parcourt par case (colonne)
                    for y in range(n):
                        # Solutions possibles col/row
                        col_rest = np.setdiff1d(suite_nb, self.base[:x, y])
                        row_rest = np.setdiff1d(suite_nb, self.base[x, :y])
                        # Solutions communes col/row
                        cr_sol = np.intersect1d(col_rest, row_rest)
                        # Solutions possibles box (3x3)
                        ns = NakedSingle(self)
                        sq_sol = ns.sq_sol(x, y)
                        # Solutions globale communes col/row/box
                        all_sol = np.intersect1d(cr_sol, np.array(list(sq_sol)))
                        # Choix random parmi solutions possibles gloable
                        self.base[x, y] = np.random.choice(all_sol, size=1)
                break
            except ValueError:
                pass
        # AFFICHAGE
        print("Complet:")
        print(self.base)
        self.base[np.random.choice([True, False], size=self.base.shape, p=[drill_rate, 1 - drill_rate])] = 0
        print("\nSudoku généré:") 
        print(self.base)

    def is_sudoku_empty(self):
        for x in range(0, len(self.base)):
            if not list(self.base[x]).count(0) == len(self.base[x]):
                return False

        return True

    def is_sudoku_complete(self):
        for x in range(0, len(self.base)):
            if list(self.base[x]).count(0) > 0:
                return False

        return True

    def is_sudoku_valid(self):
        is_valid = True
        for x in range(len(self.base)):
            for y in range(len(self.base[x])):
                ns = NakedSingle(self)
                val = self.base[x, y]
                self.base[x, y] = 0
                c_sol = ns.get_sol(x, y)
                if val != 0 and not (list(c_sol).count(val) > 0):
                    is_valid = False
                self.base[x, y] = val

        return is_valid

    def formating_sudoku(self, fc):
        x = 0
        y = 0
        for car in fc:
            if y == len(self.base[x]):
                y = 0
                x += 1
            try:
                c = int(car)
                if c >= 0 and c <= 9:
                    self.base[x,y] = c
                    y += 1
            except ValueError:
                if y != len(self.base[x]) and x != len(self.base) and not str(car) == "\n":
                    self.base[x,y] = 0
                    y += 1
                else:
                    continue
