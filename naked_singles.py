import numpy as np

tab = [[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,0,0]]

def verification(row, column, number):
    # Vérification si le nombre est valide sur sa ligne
    for i in range(0,9):
        if tab[row][i] == number:
            return False

    # Vérification si le nombre est valide sur sa colonne 
    for i in range(0,9):
        if tab[i][column] == number:
            return False

    # Vérification si le nombre est valide dans sa sous-grille
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if tab[y0+i][x0+j] == number:
                return False
    return True

def solve():
    global tab
    for row in range(0,9):
        for column in range(0,9):
            if tab[row][column] == 0:
                for number in range(1,10):
                    if verification(row, column, number):
                        tab[row][column] = number
                        solve()
                        tab[row][column] = 0
                return
    print(np.matrix(tab))
    print()
solve()