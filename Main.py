from tkinter import *
from tkinter import Button, Label, Entry
from Functions import generate_answer

def button():
    a = a_value.get()
    b = b_value.get()
    c = c_value.get()

    final_answer, solve_for = generate_answer(a, b, c)
    if solve_for == 'a':
        a_value.insert(0, str(final_answer))
    elif solve_for == 'b':
        b_value.insert(0, str(final_answer))
    elif solve_for == 'c':
        c_value.insert(0, str(final_answer))


window = Tk()
window.geometry('400x150')

Label(text='What is your C value?:').place(x=10, y=10)
c_value = Entry(window)
c_value.place(x=200, y=10)

Label(text='What is your A value?:').place(x=10, y=35)
a_value = Entry(window)
a_value.place(x=200, y=35)

Label(text='What is your B value?:').place(x=10, y=60)
b_value = Entry(window)
b_value.place(x=200, y=60)

Button(window, text='Find missing value', command=button).place(x=10, y=85)

mainloop()
