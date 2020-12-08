# -------- DAY 9 "Validate Password" --------
# Goal: Validate password if:
#     - Its length equal 9 or 12 or between of them.
#     - Contains at least one of capital letter, small letter, number and character.
from tkinter import *
import re

root = Tk()

root.title('100 Days Of Python - Day 9')
root.configure(background='#E0E0E0')

# --------------- CREATE A FRAME ---------------
frame = LabelFrame(root, text=' VALIDATE PASSWORD ', bg='#E0E0E0', fg='#00695C', font=5, padx=75, pady=75)
frame.pack(padx=20, pady=15)

infoLabel = Label(frame, text='Hi, this program for validate your password.', bg='#E0E0E0', fg='#424242', font=('time', 16, 'bold'))
infoLabel.grid(row=0, column=0, columnspan=2, pady=20)

askLabel = Label(frame, text='Enter a Password: ', bg='#E0E0E0', font=('time', 14, 'bold'))
askLabel.grid(row=1, column=0, pady=20)
e_password = Entry(frame, width=25, font=7)
e_password.grid(row=1, column=1, pady=20)


# --------------- FUNCTIONS ---------------
def validatePassword():
    if len(str(e_password.get())) < 9 or len(str(e_password.get())) > 12:
        validate_info.config(text='Your password is smaller than 9 or larger than 12!', fg='red')
    elif not re.search('[A-Z]', str(e_password.get())):
        validate_info.config(text='Missed Capital Letters!', fg='red')
    elif not re.search('[a-z]', str(e_password.get())):
        validate_info.config(text='Missed Small Letters!', fg='red')
    elif not re.search('[0-9]', str(e_password.get())):
        validate_info.config(text='Missed Numbers!', fg='red')
    elif not re.search('[~!@#$%^&*()_+=]', str(e_password.get())):
        validate_info.config(text='Missed Characters! .. (Eg: ~!@#$%^&*()_+=)', fg='red')
    else:
        validate_info.config(text='Your password is VERY GOOD', fg='#004D40')


# --------------- BUTTONS & LABEL FOR NOTES ---------------
button = Button(frame, text='Validate', bg='#009688', fg='#fff', height=2, font=3, command=validatePassword)
button.grid(row=2, column=0, columnspan=2, sticky='snew', pady=20)

validate_info = Label(frame, text='', width=45, bg='#E0E0E0', font=7)
validate_info.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
