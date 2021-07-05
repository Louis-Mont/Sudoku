from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o, rm_coll


class NakedTriples(SudokuSolver):
    def __init__(self, sudoku):
        super().__init__("Naked Triples", sudoku)

    def _solve(self, x, y):
        if 2 <= len(self.sudoku.sols[x, y]) <= 3:
            triples = [
                (self.h_triple(x, y), self.rm_h_triple),
                (self.v_triple(x, y), self.rm_v_triple),
                (self.sq_triple(x, y), self.rm_sq_triple)
            ]
            for triples_v in triples:
                triple = triples_v[0]
                if triple:
                    triples_v[1](x, y, triple)

    def h_triple(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        triple_candidate = ()
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.valid_sol(xb, yb, xb, y):
                triple = self.get_triple((xb, yb), (xb, y), triple_candidate)
                if triple and len(triple) == 3:
                    return triple
                elif self.valid_sol(xb, yb, xb, y):
                    triple_candidate = xb, y
        return False

    def v_triple(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        triple_candidate = ()
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and self.valid_sol(xb, yb, x, yb):
                triple = self.get_triple((xb, yb), (x, yb), triple_candidate)
                if triple and len(triple) == 3:
                    return triple
                elif self.valid_sol(xb, yb, x, yb):
                    triple_candidate = x, yb
        return False

    def sq_triple(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        triple_candidate = ()
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                if (xb != ax or yb != ay) and self.valid_sol(xb, yb, ax, ay):
                    triple = self.get_triple((xb, yb), (ax, ay), triple_candidate)
                    if triple and len(triple) == 3:
                        return triple
                    elif self.valid_sol(xb, yb, ax, ay):
                        triple_candidate = ax, ay
        return False

    def rm_h_triple(self, xb, yb, triple):
        """
        :type xb: int
        :type yb: int
        :type triple: set
        """
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y and self.not_triple(triple, xb, y):
                rm_coll(triple, self.sudoku.sols[xb, y])

    def rm_v_triple(self, xb, yb, triple):
        """
        :type xb: int
        :type yb: int
        :type triple: set
        """
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x and self.not_triple(triple, x, yb):
                rm_coll(triple, self.sudoku.sols[x, yb])

    def rm_sq_triple(self, xb, yb, triple):
        """
        :type xb: int
        :type yb: int
        :type triple: set
        """
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                if (xb != ax or yb != ay) and self.not_triple(triple, ax, ay):
                    rm_coll(triple, self.sudoku.sols[ax, ay])

    def valid_sol(self, xb, yb, x, y):
        """
        :type xb: int
        :type yb: int
        :type x: int
        :type y: int
        """
        sols: dict[tuple, set] = self.sudoku.sols
        try:
            if len(sols[xb, yb]) == 2:
                if len(sols[x, y]) == 3:
                    return sols[x, y].issuperset(sols[xb, yb])
                if len(sols[x, y]) == 2:
                    return len(sols[x, y] - sols[x, y]) == 1
            if len(sols[xb, yb]) == 3:
                return sols[xb, yb].issuperset(sols[x, y])
            return False
        except KeyError:
            return False

    def get_triple(self, first, second, third):
        """
        :type first: tuple
        :type second: tuple
        :type third: tuple
        """
        sols: dict[tuple, set] = self.sudoku.sols
        try:
            return sols[first].union(sols[second]).union(sols[third])
        except KeyError:
            return False

    def not_triple(self, triple, x, y):
        """
        :type triple: set
        :type x: int
        :type y: int
        """
        try:
            return not triple.issuperset(self.sudoku.sols[x, y])
        except KeyError:
            return False
