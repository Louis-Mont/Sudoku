from Core.Solver.SudokuSolver import SudokuSolver
from Core.utils import sq_o


class HiddenPairs(SudokuSolver):

    def __init__(self, sudoku):
        super().__init__("Hidden Pairs", sudoku)

    def _solve(self, x, y):
        pairs = [
            (self.h_pair(x, y), self.rm_h_pair),
            (self.v_pair(x, y), self.rm_v_pair),
            (self.sq_pair(x, y), self.rm_sq_pair)
        ]
        for pair_v in pairs:
            pair = pair_v[0]
            if pair:
                pair_v[1](x, y, pair)

    def h_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y:
                pair = self.determine_pair(xb, yb, xb, y, self.h_pair_exists)
                if pair:
                    return pair
        return False

    def v_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        for x, r in enumerate(self.sudoku.base[:, yb]):
            if xb != x:
                pair = self.determine_pair(xb, yb, x, yb, self.v_pair_exists)
                if pair:
                    return pair
        return False

    def sq_pair(self, xb, yb):
        """
        :type xb: int
        :type yb: int
        """
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                if xb != ax or yb != ay:
                    pair = self.determine_pair(xb, yb, x, yb, self.sq_pair_exists)
                    if pair:
                        return pair
        return False

    def determine_pair(self, xb, yb, x, y, orientation):
        """
        :type xb: int
        :type yb: int
        :type x: int
        :type y: int
        :type orientation: (int,int,set) -> [int,bool]
        """
        sols: dict[tuple, set] = self.sudoku.sols
        cmn = sols[xb, yb].intersection(sols[x, y])
        if len(cmn) >= 2:
            cmn = list(cmn)
            for i, s in enumerate(cmn):
                pair = {cmn[i], cmn[i + 1]}
                isalone = orientation(xb, yb, pair)
                if isalone:
                    return pair
        return False

    def h_pair_exists(self, xb, yb, pair):
        # looking for if the pair already exists in another solution
        for yp, cp in enumerate(self.sudoku.base[xb]):
            if yb != yp:
                if not self.pair_exists(pair, xb, yp):
                    continue
                else:
                    return False
        return True

    def v_pair_exists(self, xb, yb, pair):
        for xp, cp in enumerate(self.sudoku.base[:, yb]):
            if xb != xp:
                if not self.pair_exists(pair, xp, yb):
                    continue
                else:
                    return False
        return True

    def sq_pair_exists(self, xb, yb, pair):
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for xp, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + xp
            for yp, c in enumerate(r):
                ay = y0 + yp
                if xb != ax or yb != ay:
                    if not self.pair_exists(pair, ax, ay):
                        continue
                    else:
                        return False
        return True

    def pair_exists(self, pair, x, y):
        """
        Checks if the pair has smth in common with the sols[x,y]
        :type pair: set
        :type x: int
        :type y: int
        """
        try:
            if pair.isdisjoint(self.sudoku.sols[x, y]):
                return True
        except KeyError:
            return False
        return False

    def rm_h_pair(self, xb, yb, pair):
        for y, c in enumerate(self.sudoku.base[xb]):
            if yb != y:
                self.rm_pair(xb, y, pair)

    def rm_v_pair(self, xb, yb, pair):
        for x, c in enumerate(self.sudoku.base[:, yb]):
            if xb != x:
                self.rm_pair(x, yb, pair)

    def rm_sq_pair(self, xb, yb, pair):
        x0 = sq_o(xb)
        y0 = sq_o(yb)
        for x, r in enumerate(self.sudoku.base[x0:x0 + 3, y0:y0 + 3]):
            ax = x0 + x
            for y, c in enumerate(r):
                ay = y0 + y
                if xb != ax or yb != ay:
                    self.rm_pair(ax, ay, pair)

    def rm_pair(self, x, y, pair):
        """
        :type x: int
        :type y: int
        :type pair: set
        """
        sols: dict[tuple, set] = self.sudoku.sols
        if pair.issubset(sols[x, y]):
            sols[x, y] = pair
