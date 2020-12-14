# -------- DAY 13 "Roll Dice" --------
# Goal: Use random library in roll dice.
import random
from tkinter import *

root = Tk()

root.title('100 Days Of Python - Day 13')
root.configure(background='#FFF9C4')
root.geometry('450x340')

# Label for display a square dice
diceLabel = Label(root, text='', bg='#FFF9C4', font=('time', 120))


# --------------- FUNCTIONS ---------------
def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    # Display 2 dices
    diceLabel.config(text=f'{random.choice(dice)} {random.choice(dice)}')
    diceLabel.pack(padx=12, pady=48)


button = Button(root, text='Roll Dice', bg='#01579B', fg='#FFF', width=12, height=2, font=('time', 12, 'bold'),
                command=roll_dice)
button.pack(padx=12, pady=28)

root.mainloop()
