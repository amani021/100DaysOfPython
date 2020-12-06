# -------- DAY 8 "Generate Password" --------
# Goal: Learn about random library.
import random, string
from tkinter import *

root = Tk()

root.title('100 Days Of Python - Day 8')
root.configure(background='#E0E0E0')

# --------------- CREATE A FRAME ---------------
frame = LabelFrame(root, text=' GENERATE PASSWORD ', bg='#E0E0E0', fg='#00695C', font=5, padx=75, pady=75)
frame.pack(padx=20, pady=15)

infoLabel = Label(frame, text='Hi, this program for generate random password.\nYou can receive your own password from '
                              'here.\nJUST TRY IT!', bg='#E0E0E0', fg='#424242', font=('time', 16, 'bold'))
infoLabel.grid(row=0, column=0, columnspan=5, padx=4, pady=20)

askLabel = Label(frame, text='Length Of Password: ', bg='#E0E0E0', font=('time', 14, 'bold'))
askLabel.grid(row=1, column=0, padx=4, pady=20)
e_length = Entry(frame, width=25, font=7)
e_length.grid(row=1, column=1, padx=4, pady=20)


# --------------- FUNCTIONS ---------------
def generate_pass():
    password = ''

    for i in range(int(e_length.get())):\
        password += random.choice(string.ascii_letters + string.punctuation + string.digits)
    e_pass.config(text=password)


# --------------- BUTTONS & LABEL FOR PASSWORD ---------------
button = Button(frame, text='Generate', bg='#009688', fg='#fff', height=2, font=3, command=generate_pass)
button.grid(row=3, columnspan=2, sticky='snew', padx=4, pady=20)

passLabel = Label(frame, text='Your Password is: ', bg='#E0E0E0', font=('time', 14, 'bold'))
passLabel.grid(row=2, column=0, padx=4, pady=20)
e_pass = Label(frame, text='', width=25, bg='#fff', font=7)
e_pass.grid(row=2, column=1, padx=4, pady=20)

root.mainloop()
