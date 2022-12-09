from tkinter import messagebox
from math import sqrt


def error_box(error_type):
    if error_type == 1:
        text = 'Incorrect amount of values. NEEDS: 2 entered, 1 missing'
    elif error_type == 2:
        text = 'C must be the largest side'
    elif error_type == 3:
        text = 'You must enter and INT, not STR'
    messagebox.showinfo('ERROR', text)


def answer(x_num, y_num):
    x_srd = x_num ** 2
    y_srd = y_num ** 2
    if solve_for == 'c':
        final = x_srd + y_srd
        final_answer = sqrt(final)


    elif solve_for == 'a' or solve_for == 'b':
        final = x_srd - y_srd
        final_answer = sqrt(final)

    return final_answer, solve_for


def generate_answer(a, b, c):
    global x_num, y_num, solve_for, final_answer
    if c == '' and a == '' or c == '' and b == '' or b == '' and a == '':
        error_box(1)
    elif c == '':
        try:
            solve_for = 'c'
            float(a)
            x_num = float(a)
            float(b)
            y_num = float(b)
            final_answer, solve_for = answer(x_num, y_num)
        except:
            error_box(3)
    elif a == '':
        try:
            solve_for = 'a'
            float(c)
            x_num = float(c)
            float(b)
            y_num = float(b)
            if x_num > y_num:
                final_answer, solve_for = answer(x_num, y_num)
            else:
                error_box(2)
        except:
            error_box(3)
    elif b == '':
        try:
            solve_for = 'b'
            float(c)
            x_num = float(c)
            float(a)
            y_num = float(a)
            if x_num > y_num:
                final_answer, solve_for = answer(x_num, y_num)
            else:
                error_box(2)
        except:
            error_box(3)
    elif c != '' and a != '' and b != '':
        error_box(1)

    return final_answer, solve_for
