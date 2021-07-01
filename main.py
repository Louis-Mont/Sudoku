import numpy as np
import random
from Core.Sudoku import Sudoku
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.PointingPairs import PointingPairs
from tests.test_PointingPairs import TestPointingPairs

if __name__ == '__main__':
    """
    exhs = [[2, 0, 0, 0, 7, 0, 0, 3, 8],
            [0, 0, 0, 0, 0, 6, 0, 7, 0],
            [3, 0, 0, 0, 4, 0, 6, 0, 0],
            [0, 0, 8, 0, 2, 0, 7, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 7, 0, 3, 0, 4, 0, 0],
            [0, 0, 4, 0, 8, 0, 0, 0, 9],
            [0, 6, 0, 4, 0, 0, 0, 0, 0],
            [9, 1, 0, 0, 6, 0, 0, 0, 2]]
    exhs = np.array(exhs)

    sdk_hs = Sudoku(exhs)

    sdk = sdk_hs
    sdkbase = sdk.base.copy()
    print(sdkbase)
    print()

    ns = NakedSingle(sdk)
    ns.solve()
    ns.set_one_sol()
    sdkns = sdk.base.copy()
    print(sdkns)
    print((sdkbase == sdkns).all())
    print()

    hs = HiddenSingle(sdk)
    hs.solve()
    hs.set_one_sol()
    sdkhs = sdk.base.copy()
    print(sdkhs)
    print((sdkns == sdkhs).all())
    print()
    """

    test = TestPointingPairs()
    test.test_solve()
    #test.test_solve2()
