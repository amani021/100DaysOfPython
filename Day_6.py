# -------- DAY 6 "FizzBuzz" --------
# Goal: Check an input if it is divisible by (3 and 5) or (3 or 5) or none of them.
from tkinter import *

root = Tk()

root.title('100 Days Of Python - Day 6')
root.configure(background='#B3E5FC')

# --------------- CREATE A FRAME ---------------
frame = LabelFrame(root, text=' FizzBuzz ', bg='#B3E5FC', fg='#1A237E', font=15, padx=75, pady=75)
frame.pack(padx=20, pady=20)

info = Label(frame, text='Enter a number:', bg='#B3E5FC', font=.5)
info.grid(row=0, column=0, pady=5)
e_num = Entry(frame, width=21, borderwidth=3, font=7)
e_num.grid(row=1, column=0, columnspan=2, padx=3)


# --------------- FUNCTIONS ---------------
def fizz_buzz():
    try:
        if int(e_num.get()) % 3 == 0 and int(e_num.get()) % 5 == 0:
            txt.config(text='FizzBuzz')
        elif int(e_num.get()) % 3 == 0 or int(e_num.get()) % 5 == 0:
            txt.config(text='Fizz')
        else:
            txt.config(text=e_num.get())
    except ValueError:
        txt.config(text='That is NOT a number!!', bg='#B3E5FC', fg='#BF360C')


def clear():
    e_num.delete(0, END)


# --------------- BUTTONS & LABEL FOR ANSWERS ---------------
button = Button(frame, text="Check Number", bg='#F48FB1', height=2, command=fizz_buzz)
button.grid(row=2, column=0, sticky='snew', padx=2, pady=21)
button = Button(frame, text="Clear", bg='#E0E0E0', height=2, command=clear)
button.grid(row=2, column=1, sticky='snew', padx=2, pady=21)
txt = Label(frame, text='', bg='#B3E5FC', font=.5, pady=15)
txt.grid(row=3, column=0, columnspan=2)

root.mainloop()

















