import tkinter as tk
import tkinter.messagebox
import numpy as np
from Core.Sudoku import Sudoku
from Core.Solver.SudokuSolver import master_solver
from Core.Solver.BoxLineReduction import BoxLineReduction
from Core.Solver.HiddenSingle import HiddenSingle
from Core.Solver.HiddenPairs import HiddenPairs
from Core.Solver.NakedPairs import NakedPairs
from Core.Solver.NakedSingle import NakedSingle
from Core.Solver.NakedTriples import NakedTriples
from Core.Solver.PointingPairs import PointingPairs

win = tk.Tk()
win.resizable(False, False)
win.title('Sudoku Solver')
number_list = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def display_numbers():
    global number_list
    global c0_0, c0_1, c0_2, c1_0, c1_1, c1_2, c2_0, c2_1, c2_2
    global c0_3, c0_4, c0_5, c1_3, c1_4, c1_5, c2_3, c2_4, c2_5
    global c0_6, c0_7, c0_8, c1_6, c1_7, c1_8, c2_6, c2_7, c2_8
    global c3_0, c3_1, c3_2, c4_0, c4_1, c4_2, c5_0, c5_1, c5_2
    global c3_3, c3_4, c3_5, c4_3, c4_4, c4_5, c5_3, c5_4, c5_5
    global c3_6, c3_7, c3_8, c4_6, c4_7, c4_8, c5_6, c5_7, c5_8
    global c6_0, c6_1, c6_2, c7_0, c7_1, c7_2, c8_0, c8_1, c8_2
    global c6_3, c6_4, c6_5, c7_3, c7_4, c7_5, c8_3, c8_4, c8_5
    global c6_6, c6_7, c6_8, c7_6, c7_7, c7_8, c8_6, c8_7, c8_8
    for i in range(9):
        for j in range(9):
            cx_x = f'c{i}_{j}'
            number = number_list[i][j]
            if number > 0 and number < 10:
                exec(f'{cx_x}.delete("all")')
                exec(f'{cx_x}.create_text(25,25, text = str({number}), font = "Times 25 bold")')
            else:
                exec(f'{cx_x}.delete("all")')


def create_frames():
    #           Frames
    global frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9
    frame_1 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_2 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_3 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_4 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_5 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_6 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_7 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_8 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)
    frame_9 = tk.Frame(win, bd=3, relief='solid', borderwidth=1)


create_frames()


def display_frames():
    #           Displaying Frames
    global frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9
    frame_1.grid(row=0, column=0)
    frame_2.grid(row=0, column=1)
    frame_3.grid(row=0, column=2)
    frame_4.grid(row=1, column=0)
    frame_5.grid(row=1, column=1)
    frame_6.grid(row=1, column=2)
    frame_7.grid(row=2, column=0)
    frame_8.grid(row=2, column=1)
    frame_9.grid(row=2, column=2)


display_frames()


def create_canvass():
    #       Frame 1 canvas
    global c0_0, c0_1, c0_2, c1_0, c1_1, c1_2, c2_0, c2_1, c2_2
    c0_0 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c0_1 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c0_2 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c1_0 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c1_1 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c1_2 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c2_0 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c2_1 = tk.Canvas(frame_1, bg='White', width=50, height=50)
    c2_2 = tk.Canvas(frame_1, bg='White', width=50, height=50)

    #       Frame 2 canvas
    global c0_3, c0_4, c0_5, c1_3, c1_4, c1_5, c2_3, c2_4, c2_5
    c0_3 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c0_4 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c0_5 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c1_3 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c1_4 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c1_5 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c2_3 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c2_4 = tk.Canvas(frame_2, bg='White', width=50, height=50)
    c2_5 = tk.Canvas(frame_2, bg='White', width=50, height=50)

    #       Frame 3 canvas
    global c0_6, c0_7, c0_8, c1_6, c1_7, c1_8, c2_6, c2_7, c2_8
    c0_6 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c0_7 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c0_8 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c1_6 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c1_7 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c1_8 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c2_6 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c2_7 = tk.Canvas(frame_3, bg='White', width=50, height=50)
    c2_8 = tk.Canvas(frame_3, bg='White', width=50, height=50)

    #       Frame 4 canvas
    global c3_0, c3_1, c3_2, c4_0, c4_1, c4_2, c5_0, c5_1, c5_2
    c3_0 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c3_1 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c3_2 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c4_0 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c4_1 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c4_2 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c5_0 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c5_1 = tk.Canvas(frame_4, bg='White', width=50, height=50)
    c5_2 = tk.Canvas(frame_4, bg='White', width=50, height=50)

    #       Frame 5 canvas
    global c3_3, c3_4, c3_5, c4_3, c4_4, c4_5, c5_3, c5_4, c5_5
    c3_3 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c3_4 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c3_5 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c4_3 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c4_4 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c4_5 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c5_3 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c5_4 = tk.Canvas(frame_5, bg='White', width=50, height=50)
    c5_5 = tk.Canvas(frame_5, bg='White', width=50, height=50)

    #       Frame 6 canvas
    global c3_6, c3_7, c3_8, c4_6, c4_7, c4_8, c5_6, c5_7, c5_8
    c3_6 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c3_7 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c3_8 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c4_6 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c4_7 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c4_8 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c5_6 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c5_7 = tk.Canvas(frame_6, bg='White', width=50, height=50)
    c5_8 = tk.Canvas(frame_6, bg='White', width=50, height=50)

    #       Frame 7 canvas
    global c6_0, c6_1, c6_2, c7_0, c7_1, c7_2, c8_0, c8_1, c8_2
    c6_0 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c6_1 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c6_2 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c7_0 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c7_1 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c7_2 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c8_0 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c8_1 = tk.Canvas(frame_7, bg='White', width=50, height=50)
    c8_2 = tk.Canvas(frame_7, bg='White', width=50, height=50)

    #       Frame 8 canvas
    global c6_3, c6_4, c6_5, c7_3, c7_4, c7_5, c8_3, c8_4, c8_5
    c6_3 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c6_4 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c6_5 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c7_3 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c7_4 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c7_5 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c8_3 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c8_4 = tk.Canvas(frame_8, bg='White', width=50, height=50)
    c8_5 = tk.Canvas(frame_8, bg='White', width=50, height=50)

    #       Frame 9 canvas
    global c6_6, c6_7, c6_8, c7_6, c7_7, c7_8, c8_6, c8_7, c8_8
    c6_6 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c6_7 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c6_8 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c7_6 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c7_7 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c7_8 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c8_6 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c8_7 = tk.Canvas(frame_9, bg='White', width=50, height=50)
    c8_8 = tk.Canvas(frame_9, bg='White', width=50, height=50)


create_canvass()


def display_canvass():
    #       Frame 1 Display
    global c0_0, c0_1, c0_2, c1_0, c1_1, c1_2, c2_0, c2_1, c2_2
    global c0_3, c0_4, c0_5, c1_3, c1_4, c1_5, c2_3, c2_4, c2_5
    global c0_6, c0_7, c0_8, c1_6, c1_7, c1_8, c2_6, c2_7, c2_8
    global c3_0, c3_1, c3_2, c4_0, c4_1, c4_2, c5_0, c5_1, c5_2
    global c3_3, c3_4, c3_5, c4_3, c4_4, c4_5, c5_3, c5_4, c5_5
    global c3_6, c3_7, c3_8, c4_6, c4_7, c4_8, c5_6, c5_7, c5_8
    global c6_0, c6_1, c6_2, c7_0, c7_1, c7_2, c8_0, c8_1, c8_2
    global c6_3, c6_4, c6_5, c7_3, c7_4, c7_5, c8_3, c8_4, c8_5
    global c6_6, c6_7, c6_8, c7_6, c7_7, c7_8, c8_6, c8_7, c8_8

    #       Frame 1 Display
    c0_0.grid(row=0, column=0)
    c0_1.grid(row=0, column=1)
    c0_2.grid(row=0, column=2)
    c1_0.grid(row=1, column=0)
    c1_1.grid(row=1, column=1)
    c1_2.grid(row=1, column=2)
    c2_0.grid(row=2, column=0)
    c2_1.grid(row=2, column=1)
    c2_2.grid(row=2, column=2)

    #       Frame 2 Display
    c0_3.grid(row=0, column=0)
    c0_4.grid(row=0, column=1)
    c0_5.grid(row=0, column=2)
    c1_3.grid(row=1, column=0)
    c1_4.grid(row=1, column=1)
    c1_5.grid(row=1, column=2)
    c2_3.grid(row=2, column=0)
    c2_4.grid(row=2, column=1)
    c2_5.grid(row=2, column=2)

    #       Frame 3 Display
    c0_6.grid(row=0, column=0)
    c0_7.grid(row=0, column=1)
    c0_8.grid(row=0, column=2)
    c1_6.grid(row=1, column=0)
    c1_7.grid(row=1, column=1)
    c1_8.grid(row=1, column=2)
    c2_6.grid(row=2, column=0)
    c2_7.grid(row=2, column=1)
    c2_8.grid(row=2, column=2)

    #       Frame 4 Display
    c3_0.grid(row=0, column=0)
    c3_1.grid(row=0, column=1)
    c3_2.grid(row=0, column=2)
    c4_0.grid(row=1, column=0)
    c4_1.grid(row=1, column=1)
    c4_2.grid(row=1, column=2)
    c5_0.grid(row=2, column=0)
    c5_1.grid(row=2, column=1)
    c5_2.grid(row=2, column=2)

    #       Frame 5 Display
    c3_3.grid(row=0, column=0)
    c3_4.grid(row=0, column=1)
    c3_5.grid(row=0, column=2)
    c4_3.grid(row=1, column=0)
    c4_4.grid(row=1, column=1)
    c4_5.grid(row=1, column=2)
    c5_3.grid(row=2, column=0)
    c5_4.grid(row=2, column=1)
    c5_5.grid(row=2, column=2)

    #       Frame 6 Display
    c3_6.grid(row=0, column=0)
    c3_7.grid(row=0, column=1)
    c3_8.grid(row=0, column=2)
    c4_6.grid(row=1, column=0)
    c4_7.grid(row=1, column=1)
    c4_8.grid(row=1, column=2)
    c5_6.grid(row=2, column=0)
    c5_7.grid(row=2, column=1)
    c5_8.grid(row=2, column=2)

    #       Frame 7 Display
    c6_0.grid(row=0, column=0)
    c6_1.grid(row=0, column=1)
    c6_2.grid(row=0, column=2)
    c7_0.grid(row=1, column=0)
    c7_1.grid(row=1, column=1)
    c7_2.grid(row=1, column=2)
    c8_0.grid(row=2, column=0)
    c8_1.grid(row=2, column=1)
    c8_2.grid(row=2, column=2)

    #       Frame 8 Display
    c6_3.grid(row=0, column=0)
    c6_4.grid(row=0, column=1)
    c6_5.grid(row=0, column=2)
    c7_3.grid(row=1, column=0)
    c7_4.grid(row=1, column=1)
    c7_5.grid(row=1, column=2)
    c8_3.grid(row=2, column=0)
    c8_4.grid(row=2, column=1)
    c8_5.grid(row=2, column=2)

    #       Frame 9 Display
    c6_6.grid(row=0, column=0)
    c6_7.grid(row=0, column=1)
    c6_8.grid(row=0, column=2)
    c7_6.grid(row=1, column=0)
    c7_7.grid(row=1, column=1)
    c7_8.grid(row=1, column=2)
    c8_6.grid(row=2, column=0)
    c8_7.grid(row=2, column=1)
    c8_8.grid(row=2, column=2)


display_canvass()

f_number = [0, 0]


def change_focus(arg1):
    global f_number
    exec(f'{arg1}.focus_set()')
    f_number = [int(arg1[1]), int(arg1[3])]


def change_text(event):
    global f_number
    global number_list
    exec(f'c{f_number[0]}_{f_number[1]}.delete("all")')
    cx_x = f'c{f_number[0]}_{f_number[1]}'
    number_list[f_number[0]][f_number[1]] = int(event.char)
    exec(f'{cx_x}.create_text(25,25, text = event.char, font = "Times 25 bold")')


def focus_mouse():
    global c0_0, c0_1, c0_2, c1_0, c1_1, c1_2, c2_0, c2_1, c2_2
    global c0_3, c0_4, c0_5, c1_3, c1_4, c1_5, c2_3, c2_4, c2_5
    global c0_6, c0_7, c0_8, c1_6, c1_7, c1_8, c2_6, c2_7, c2_8
    global c3_0, c3_1, c3_2, c4_0, c4_1, c4_2, c5_0, c5_1, c5_2
    global c3_3, c3_4, c3_5, c4_3, c4_4, c4_5, c5_3, c5_4, c5_5
    global c3_6, c3_7, c3_8, c4_6, c4_7, c4_8, c5_6, c5_7, c5_8
    global c6_0, c6_1, c6_2, c7_0, c7_1, c7_2, c8_0, c8_1, c8_2
    global c6_3, c6_4, c6_5, c7_3, c7_4, c7_5, c8_3, c8_4, c8_5
    global c6_6, c6_7, c6_8, c7_6, c7_7, c7_8, c8_6, c8_7, c8_8

    #           FOCUSING THE MOUSE
    #       Row 1
    c0_0.bind('<Button-1>', lambda x: change_focus('c0_0'))
    c0_1.bind('<Button-1>', lambda x: change_focus('c0_1'))
    c0_2.bind('<Button-1>', lambda x: change_focus('c0_2'))
    c0_3.bind('<Button-1>', lambda x: change_focus('c0_3'))
    c0_4.bind('<Button-1>', lambda x: change_focus('c0_4'))
    c0_5.bind('<Button-1>', lambda x: change_focus('c0_5'))
    c0_6.bind('<Button-1>', lambda x: change_focus('c0_6'))
    c0_7.bind('<Button-1>', lambda x: change_focus('c0_7'))
    c0_8.bind('<Button-1>', lambda x: change_focus('c0_8'))

    #       Row 2
    c1_0.bind('<Button-1>', lambda x: change_focus('c1_0'))
    c1_1.bind('<Button-1>', lambda x: change_focus('c1_1'))
    c1_2.bind('<Button-1>', lambda x: change_focus('c1_2'))
    c1_3.bind('<Button-1>', lambda x: change_focus('c1_3'))
    c1_4.bind('<Button-1>', lambda x: change_focus('c1_4'))
    c1_5.bind('<Button-1>', lambda x: change_focus('c1_5'))
    c1_6.bind('<Button-1>', lambda x: change_focus('c1_6'))
    c1_7.bind('<Button-1>', lambda x: change_focus('c1_7'))
    c1_8.bind('<Button-1>', lambda x: change_focus('c1_8'))

    #       Row 3
    c2_0.bind('<Button-1>', lambda x: change_focus('c2_0'))
    c2_1.bind('<Button-1>', lambda x: change_focus('c2_1'))
    c2_2.bind('<Button-1>', lambda x: change_focus('c2_2'))
    c2_3.bind('<Button-1>', lambda x: change_focus('c2_3'))
    c2_4.bind('<Button-1>', lambda x: change_focus('c2_4'))
    c2_5.bind('<Button-1>', lambda x: change_focus('c2_5'))
    c2_6.bind('<Button-1>', lambda x: change_focus('c2_6'))
    c2_7.bind('<Button-1>', lambda x: change_focus('c2_7'))
    c2_8.bind('<Button-1>', lambda x: change_focus('c2_8'))

    #       Row 4
    c3_0.bind('<Button-1>', lambda x: change_focus('c3_0'))
    c3_1.bind('<Button-1>', lambda x: change_focus('c3_1'))
    c3_2.bind('<Button-1>', lambda x: change_focus('c3_2'))
    c3_3.bind('<Button-1>', lambda x: change_focus('c3_3'))
    c3_4.bind('<Button-1>', lambda x: change_focus('c3_4'))
    c3_5.bind('<Button-1>', lambda x: change_focus('c3_5'))
    c3_6.bind('<Button-1>', lambda x: change_focus('c3_6'))
    c3_7.bind('<Button-1>', lambda x: change_focus('c3_7'))
    c3_8.bind('<Button-1>', lambda x: change_focus('c3_8'))

    #       Row 5
    c4_0.bind('<Button-1>', lambda x: change_focus('c4_0'))
    c4_1.bind('<Button-1>', lambda x: change_focus('c4_1'))
    c4_2.bind('<Button-1>', lambda x: change_focus('c4_2'))
    c4_3.bind('<Button-1>', lambda x: change_focus('c4_3'))
    c4_4.bind('<Button-1>', lambda x: change_focus('c4_4'))
    c4_5.bind('<Button-1>', lambda x: change_focus('c4_5'))
    c4_6.bind('<Button-1>', lambda x: change_focus('c4_6'))
    c4_7.bind('<Button-1>', lambda x: change_focus('c4_7'))
    c4_8.bind('<Button-1>', lambda x: change_focus('c4_8'))

    #       Row 6
    c5_0.bind('<Button-1>', lambda x: change_focus('c5_0'))
    c5_1.bind('<Button-1>', lambda x: change_focus('c5_1'))
    c5_2.bind('<Button-1>', lambda x: change_focus('c5_2'))
    c5_3.bind('<Button-1>', lambda x: change_focus('c5_3'))
    c5_4.bind('<Button-1>', lambda x: change_focus('c5_4'))
    c5_5.bind('<Button-1>', lambda x: change_focus('c5_5'))
    c5_6.bind('<Button-1>', lambda x: change_focus('c5_6'))
    c5_7.bind('<Button-1>', lambda x: change_focus('c5_7'))
    c5_8.bind('<Button-1>', lambda x: change_focus('c5_8'))

    #       Row 7
    c6_0.bind('<Button-1>', lambda x: change_focus('c6_0'))
    c6_1.bind('<Button-1>', lambda x: change_focus('c6_1'))
    c6_2.bind('<Button-1>', lambda x: change_focus('c6_2'))
    c6_3.bind('<Button-1>', lambda x: change_focus('c6_3'))
    c6_4.bind('<Button-1>', lambda x: change_focus('c6_4'))
    c6_5.bind('<Button-1>', lambda x: change_focus('c6_5'))
    c6_6.bind('<Button-1>', lambda x: change_focus('c6_6'))
    c6_7.bind('<Button-1>', lambda x: change_focus('c6_7'))
    c6_8.bind('<Button-1>', lambda x: change_focus('c6_8'))

    #       Row 8
    c7_0.bind('<Button-1>', lambda x: change_focus('c7_0'))
    c7_1.bind('<Button-1>', lambda x: change_focus('c7_1'))
    c7_2.bind('<Button-1>', lambda x: change_focus('c7_2'))
    c7_3.bind('<Button-1>', lambda x: change_focus('c7_3'))
    c7_4.bind('<Button-1>', lambda x: change_focus('c7_4'))
    c7_5.bind('<Button-1>', lambda x: change_focus('c7_5'))
    c7_6.bind('<Button-1>', lambda x: change_focus('c7_6'))
    c7_7.bind('<Button-1>', lambda x: change_focus('c7_7'))
    c7_8.bind('<Button-1>', lambda x: change_focus('c7_8'))

    #       Row 9
    c8_0.bind('<Button-1>', lambda x: change_focus('c8_0'))
    c8_1.bind('<Button-1>', lambda x: change_focus('c8_1'))
    c8_2.bind('<Button-1>', lambda x: change_focus('c8_2'))
    c8_3.bind('<Button-1>', lambda x: change_focus('c8_3'))
    c8_4.bind('<Button-1>', lambda x: change_focus('c8_4'))
    c8_5.bind('<Button-1>', lambda x: change_focus('c8_5'))
    c8_6.bind('<Button-1>', lambda x: change_focus('c8_6'))
    c8_7.bind('<Button-1>', lambda x: change_focus('c8_7'))
    c8_8.bind('<Button-1>', lambda x: change_focus('c8_8'))


focus_mouse()


def bind_text():
    global c0_0, c0_1, c0_2, c1_0, c1_1, c1_2, c2_0, c2_1, c2_2
    global c0_3, c0_4, c0_5, c1_3, c1_4, c1_5, c2_3, c2_4, c2_5
    global c0_6, c0_7, c0_8, c1_6, c1_7, c1_8, c2_6, c2_7, c2_8
    global c3_0, c3_1, c3_2, c4_0, c4_1, c4_2, c5_0, c5_1, c5_2
    global c3_3, c3_4, c3_5, c4_3, c4_4, c4_5, c5_3, c5_4, c5_5
    global c3_6, c3_7, c3_8, c4_6, c4_7, c4_8, c5_6, c5_7, c5_8
    global c6_0, c6_1, c6_2, c7_0, c7_1, c7_2, c8_0, c8_1, c8_2
    global c6_3, c6_4, c6_5, c7_3, c7_4, c7_5, c8_3, c8_4, c8_5
    global c6_6, c6_7, c6_8, c7_6, c7_7, c7_8, c8_6, c8_7, c8_8

    #       Row 1
    c0_0.bind('<Key>', change_text)
    c0_1.bind('<Key>', change_text)
    c0_2.bind('<Key>', change_text)
    c0_3.bind('<Key>', change_text)
    c0_4.bind('<Key>', change_text)
    c0_5.bind('<Key>', change_text)
    c0_6.bind('<Key>', change_text)
    c0_7.bind('<Key>', change_text)
    c0_8.bind('<Key>', change_text)

    #       Row 2
    c1_0.bind('<Key>', change_text)
    c1_1.bind('<Key>', change_text)
    c1_2.bind('<Key>', change_text)
    c1_3.bind('<Key>', change_text)
    c1_4.bind('<Key>', change_text)
    c1_5.bind('<Key>', change_text)
    c1_6.bind('<Key>', change_text)
    c1_7.bind('<Key>', change_text)
    c1_8.bind('<Key>', change_text)

    #       Row 3
    c2_0.bind('<Key>', change_text)
    c2_1.bind('<Key>', change_text)
    c2_2.bind('<Key>', change_text)
    c2_3.bind('<Key>', change_text)
    c2_4.bind('<Key>', change_text)
    c2_5.bind('<Key>', change_text)
    c2_6.bind('<Key>', change_text)
    c2_7.bind('<Key>', change_text)
    c2_8.bind('<Key>', change_text)

    #       Row 4
    c3_0.bind('<Key>', change_text)
    c3_1.bind('<Key>', change_text)
    c3_2.bind('<Key>', change_text)
    c3_3.bind('<Key>', change_text)
    c3_4.bind('<Key>', change_text)
    c3_5.bind('<Key>', change_text)
    c3_6.bind('<Key>', change_text)
    c3_7.bind('<Key>', change_text)
    c3_8.bind('<Key>', change_text)

    #       Row 5
    c4_0.bind('<Key>', change_text)
    c4_1.bind('<Key>', change_text)
    c4_2.bind('<Key>', change_text)
    c4_3.bind('<Key>', change_text)
    c4_4.bind('<Key>', change_text)
    c4_5.bind('<Key>', change_text)
    c4_6.bind('<Key>', change_text)
    c4_7.bind('<Key>', change_text)
    c4_8.bind('<Key>', change_text)

    #       Row 6
    c5_0.bind('<Key>', change_text)
    c5_1.bind('<Key>', change_text)
    c5_2.bind('<Key>', change_text)
    c5_3.bind('<Key>', change_text)
    c5_4.bind('<Key>', change_text)
    c5_5.bind('<Key>', change_text)
    c5_6.bind('<Key>', change_text)
    c5_7.bind('<Key>', change_text)
    c5_8.bind('<Key>', change_text)

    #       Row 7
    c6_0.bind('<Key>', change_text)
    c6_1.bind('<Key>', change_text)
    c6_2.bind('<Key>', change_text)
    c6_3.bind('<Key>', change_text)
    c6_4.bind('<Key>', change_text)
    c6_5.bind('<Key>', change_text)
    c6_6.bind('<Key>', change_text)
    c6_7.bind('<Key>', change_text)
    c6_8.bind('<Key>', change_text)

    #       Row 8
    c7_0.bind('<Key>', change_text)
    c7_1.bind('<Key>', change_text)
    c7_2.bind('<Key>', change_text)
    c7_3.bind('<Key>', change_text)
    c7_4.bind('<Key>', change_text)
    c7_5.bind('<Key>', change_text)
    c7_6.bind('<Key>', change_text)
    c7_7.bind('<Key>', change_text)
    c7_8.bind('<Key>', change_text)

    #       Row 9
    c8_0.bind('<Key>', change_text)
    c8_1.bind('<Key>', change_text)
    c8_2.bind('<Key>', change_text)
    c8_3.bind('<Key>', change_text)
    c8_4.bind('<Key>', change_text)
    c8_5.bind('<Key>', change_text)
    c8_6.bind('<Key>', change_text)
    c8_7.bind('<Key>', change_text)
    c8_8.bind('<Key>', change_text)


bind_text()


def clear_list_all():
    global number_list
    global c0_0, c0_1, c0_2, c1_0, c1_1, c1_2, c2_0, c2_1, c2_2
    global c0_3, c0_4, c0_5, c1_3, c1_4, c1_5, c2_3, c2_4, c2_5
    global c0_6, c0_7, c0_8, c1_6, c1_7, c1_8, c2_6, c2_7, c2_8
    global c3_0, c3_1, c3_2, c4_0, c4_1, c4_2, c5_0, c5_1, c5_2
    global c3_3, c3_4, c3_5, c4_3, c4_4, c4_5, c5_3, c5_4, c5_5
    global c3_6, c3_7, c3_8, c4_6, c4_7, c4_8, c5_6, c5_7, c5_8
    global c6_0, c6_1, c6_2, c7_0, c7_1, c7_2, c8_0, c8_1, c8_2
    global c6_3, c6_4, c6_5, c7_3, c7_4, c7_5, c8_3, c8_4, c8_5
    global c6_6, c6_7, c6_8, c7_6, c7_7, c7_8, c8_6, c8_7, c8_8
    for i in range(9):
        for j in range(9):
            cy_y = f'c{i}_{j}'
            exec(f'{cy_y}.delete("all")')

    number_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def clear_list_sp():
    global number_list, f_number
    global c0_0, c0_1, c0_2, c1_0, c1_1, c1_2, c2_0, c2_1, c2_2
    global c0_3, c0_4, c0_5, c1_3, c1_4, c1_5, c2_3, c2_4, c2_5
    global c0_6, c0_7, c0_8, c1_6, c1_7, c1_8, c2_6, c2_7, c2_8
    global c3_0, c3_1, c3_2, c4_0, c4_1, c4_2, c5_0, c5_1, c5_2
    global c3_3, c3_4, c3_5, c4_3, c4_4, c4_5, c5_3, c5_4, c5_5
    global c3_6, c3_7, c3_8, c4_6, c4_7, c4_8, c5_6, c5_7, c5_8
    global c6_0, c6_1, c6_2, c7_0, c7_1, c7_2, c8_0, c8_1, c8_2
    global c6_3, c6_4, c6_5, c7_3, c7_4, c7_5, c8_3, c8_4, c8_5
    global c6_6, c6_7, c6_8, c7_6, c7_7, c7_8, c8_6, c8_7, c8_8
    cy_y = f'c{f_number[0]}_{f_number[1]}'
    exec(f'{cy_y}.delete("all")')
    number_list[f_number[0]][f_number[1]] = 0


def solve_sudoku():
    global number_list
    """number_list = [[2, 0, 0, 0, 7, 0, 0, 3, 8],
                   [0, 0, 0, 0, 0, 6, 0, 7, 0],
                   [3, 0, 0, 0, 4, 0, 6, 0, 0],
                   [0, 0, 8, 0, 2, 0, 7, 0, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 6],
                   [0, 0, 7, 0, 3, 0, 4, 0, 0],
                   [0, 0, 4, 0, 8, 0, 0, 0, 9],
                   [0, 6, 0, 4, 0, 0, 0, 0, 0],
                   [9, 1, 0, 0, 6, 0, 0, 0, 2]]"""
    number_list = [[0, 7, 0, 4, 0, 8, 0, 2, 9],
                   [0, 0, 2, 0, 0, 0, 0, 0, 4],
                   [8, 5, 4, 0, 2, 0, 0, 0, 7],
                   [0, 0, 8, 3, 7, 4, 2, 0, 0],
                   [0, 2, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 3, 2, 6, 1, 7, 0, 0],
                   [0, 0, 0, 0, 9, 3, 6, 1, 2],
                   [2, 0, 0, 0, 0, 0, 4, 0, 3],
                   [1, 3, 0, 6, 4, 2, 0, 7, 0]]
    sdk = Sudoku(np.array(number_list))
    if sdk.is_sudoku_valid():
        step = 0
        while not sdk.is_sudoku_complete() and step < 200:
            solvers = [NakedSingle, NakedPairs, NakedTriples, PointingPairs, BoxLineReduction]
            master_solver(solvers, sdk)
            number_list = sdk.base
            step += 1
    if not sdk.is_sudoku_valid():
        tkinter.messagebox.showerror('ERREUR', "Il y a une erreur dans votre Sudoku")
    display_numbers()


def exit():
    win.destroy()


OptionList = ["Méthode 1 ", "méthode 2", "méthode 3"]

button_choice = tk.OptionMenu(win, OptionList[0], *OptionList)
button_solve = tk.Button(win, text='Résoudre le Sudoku', command=lambda: solve_sudoku())
button_clear_all = tk.Button(win, text='Vider le Sudoku', command=clear_list_all)
button_clear = tk.Button(win, text='Effacer la case', command=clear_list_sp)
c1 = tk.Checkbutton(win, text='solver1', onvalue=1, offvalue=0, command=clear_list_sp)
c2 = tk.Checkbutton(win, text='solver2', onvalue=1, offvalue=0, command=clear_list_sp)
c3 = tk.Checkbutton(win, text='solver3', onvalue=1, offvalue=0, command=clear_list_sp)
c4 = tk.Checkbutton(win, text='solver4', onvalue=1, offvalue=0, command=clear_list_sp)
c5 = tk.Checkbutton(win, text='solver5', onvalue=1, offvalue=0, command=clear_list_sp)

button_solve.grid(row=4, column=0)
button_clear_all.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
c1.grid(row=0, column=3)
c2.grid(row=1, column=3)
c3.grid(row=2, column=3)
c4.grid(row=3, column=3)
c5.grid(row=4, column=3)

menu_file = tk.Menu(win)
edit_bar = tk.Menu(menu_file, tearoff=False)
edit_bar.add_command(label='Vider le Sudoku', command=clear_list_all)
edit_bar.add_command(label='Résoudre le Sudoku', command=solve_sudoku)
edit_bar.add_command(label='Quitter', command=exit)
menu_file.add_cascade(label='Options', menu=edit_bar)

display_numbers()
win.config(menu=menu_file)
win.mainloop()
