def sq_o(n):
    return (n // 3) * 3


def tryremove(c, v):
    try:
        c.remove(v)
    except ValueError:
        pass
    except KeyError:
        # TODO : Not Good Sudoku
        pass
    return c
