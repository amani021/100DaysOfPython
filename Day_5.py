# -------- DAY 5 "" --------
# Goal: Using turtle to draw 2 shapes (star & circle) when click on button
import turtle
import random
from tkinter import *

terry = turtle.Turtle()
root = Tk()

root.title('100 Days Of Python - Day 5')
root.configure(background='#E6EE9C')


# --------------- FUNCTIONS ---------------
def drawStar():
    colors = ['pink', 'grey', 'cyan', 'purple']
    terry.penup()
    terry.back(220)
    terry.left(120)
    terry.pendown()
    color = random.choice(colors)
    # for loop to draw a star
    for i in range(2, 7):
        terry.width(i)
        terry.color(color)
        terry.forward(120)
        terry.left(144)
    terry.hideturtle()


def drawCircle():
    colors = ['red', 'orange', 'green', 'blue', 'purple']
    terry.penup()
    terry.back(30)
    terry.pendown()
    A = range(3, 6, 2)

    for x in A:
        color = random.choice(colors)
        terry.width(x)
        terry.color(color)
        terry.circle(x ** 2.5)
        terry.penup()
        terry.right(x * -8)
        terry.back(21)
        terry.up()
        terry.pendown()
    terry.hideturtle()


# --------------- BUTTONS ---------------
star = Button(root, text='Draw Star', bg='#00BFA5', width=20, height=3, font=14, command=drawStar)
star.grid(row=1, column=0, sticky='snew', padx=12, pady=25)
circle = Button(root, text="Draw Circle", bg='#00BFA5', width=20, height=3, font=14, command=drawCircle)
circle.grid(row=1, column=1, sticky='snew', padx=12, pady=25)

root.mainloop()
