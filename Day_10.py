# -------- DAY 10 "Add & Subtract" --------
# Goal: Do 2 operations (plus (+) and minus (-)) in a special way
from tkinter import *

root = Tk()

root.title('100 Days Of Python - Day 10')
root.configure(background='#424242')

# --------------- CREATE A FRAME ,, AS A FACE ---------------
frame = LabelFrame(root, bg='#FFE0B2', padx=15, pady=15)
frame.pack(padx=20, pady=15)


# --------------- FUNCTIONS ---------------
def addition():
    global totalNum, e_num1, e_num2, innerFrame
    # Create new button to do an operation
    totalNum = Button(frame, bg='#FFE0B2', width=15, height=2, font=14, command=lambda: total('+'))
    totalNum.grid(row=1, column=0, sticky='snew', padx=12, pady=25)
    # Create inner frame contains 2 entry elements
    innerFrame = LabelFrame(frame, bg='#000', font=5, padx=1, pady=1)
    innerFrame.grid(row=1, column=0, padx=12, pady=25)
    # Entry elements to write in it any numbers
    e_num1 = Entry(innerFrame, width=6, font=14)
    e_num1.grid(row=0, column=0, padx=3)
    e_num2 = Entry(innerFrame, width=6, font=14)
    e_num2.grid(row=0, column=1, padx=3)


def subtract():
    global totalNum, e_num1, e_num2, innerFrame
    # Create new button to do an operation
    totalNum = Button(frame, bg='#FFE0B2', width=15, height=2, font=14, command=lambda: total('-'))
    totalNum.grid(row=1, column=2, sticky='snew', padx=12, pady=25)
    # Create inner frame contains 2 entry elements
    innerFrame = LabelFrame(frame, bg='#000', font=5, padx=1, pady=1)
    innerFrame.grid(row=1, column=2, padx=12, pady=25)
    # Entry elements to write in it any numbers
    e_num1 = Entry(innerFrame, width=6, font=14)
    e_num1.grid(row=0, column=0, padx=3)
    e_num2 = Entry(innerFrame, width=6, font=14)
    e_num2.grid(row=0, column=1, padx=3)


# This function will called by lambda function
def total(x):
    try:
        if x == '+':
            addNum = int(e_num1.get()) + int(e_num2.get())
            answer.config(text=f'{e_num1.get()} + {e_num2.get()} = {addNum}', fg='#FFF')
        elif x == '-':
            subNum = int(e_num1.get()) - int(e_num2.get())
            answer.config(text=f'{e_num1.get()} - {e_num2.get()} = {subNum}', fg='#FFF')
    except ValueError:
        answer.config(text='Enter JUST a number!', fg='red')


# Clear button and the inner frame with all within it plus the answer in the label
def clear():
    answer.config(text='')
    totalNum.destroy()
    innerFrame.destroy()


infoLabel = Label(frame, text='Test Yourself & Have Fun', width=25, height=2, bg='#FFE0B2', fg='#424242', font=('arial', 21, 'bold'))
infoLabel.grid(row=0, column=0, columnspan=3)

# --------------- BUTTONS FOR OPERATIONS ,, AS EYES ---------------
addition = Button(frame, text='Add ( + )', bg='#00BFA5', width=15, height=2, font=14, command=addition)
addition.grid(row=1, column=0, sticky='snew', padx=12, pady=25)
subtract = Button(frame, text="Subtract ( - )", bg='#00BFA5', width=15, height=2, font=14, command=subtract)
subtract.grid(row=1, column=2, sticky='snew', padx=12, pady=25)

# --------------- BUTTON FOR CLEAR ,, AS A NOSE ---------------
clear = Button(frame, text='Clear', bg='#FFE0B2', bd=3, width=5, height=2, font=7, command=clear)
clear.grid(row=2, column=1, pady=5)

# --------------- LABEL FOR ANSWER ,, AS A MOUTH ---------------
answer = Label(frame, text='', width=21, height=2, bg='#F06292', font=('arial', 21, 'bold'))
answer.grid(row=3, column=0, columnspan=3, padx=12, pady=25)

root.mainloop()