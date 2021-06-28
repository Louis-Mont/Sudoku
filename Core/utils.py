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


def rm_coll(r_items, items):
    """
    :param r_items: the items you want to be removed from the list
    :param items: the list where the items are removed
    """
    for s in r_items:
        tryremove(items, s)
    return items
