# -------- DAY 12 "Passenger Week" --------
# Goal: Calculate the passenger travel days to be in weeks
from tkinter import *

root = Tk()

root.title('100 Days Of Python - Day 12')
root.configure(background='#E8EAF6')

# --------------- CREATE A FRAME ---------------
frame = LabelFrame(root, text=' PASSENGER WEEK ', bg='#E8EAF6', fg='#1A237E', font=5, padx=55, pady=45)
frame.pack(padx=25, pady=15)

infoLabel = Label(frame, text='Hello Passenger,\n\nThis program for calculate your travel days\nto be in weeks.',
                  bg='#E8EAF6', fg='#424242', font=('time', 16, 'bold'))
infoLabel.grid(row=0, column=0, columnspan=5, padx=4, pady=15)

dayLabel = Label(frame, text='Number Of Days: ', bg='#E8EAF6', font=('time', 14, 'bold'))
dayLabel.grid(row=1, column=0, padx=4, pady=20)
e_days = Entry(frame, width=17, font=7)
e_days.grid(row=1, column=1, padx=2, pady=20, ipady=4)
unit = Label(frame, text='Day/s.', width=5, bg='#E8EAF6', font=('time', 13))
unit.grid(row=1, column=2, pady=20)


# --------------- FUNCTIONS ---------------
def passenger_week():
    try:
        week = int(e_days.get()) // 7
        day = int(e_days.get()) % 7
        # Conditions for all possibilities for the outcome of operations above
        if week < 1 and day == 1:
            weeks.config(text=f'{day} day.', fg='#000')
        elif week < 1 < day:
            weeks.config(text=f'{day} days.', fg='#000')
        ###
        elif week == 1 and day == 1:
            weeks.config(text=f'{week} week and {day} day.', fg='#000')
        elif week == 1 and day > 1:
            weeks.config(text=f'{week} week and {day} days.', fg='#000')
        ###
        elif week == 1 and day < 1:
            weeks.config(text=f'{week} week.', fg='#000')
        elif week > 1 > day:
            weeks.config(text=f'{week} weeks.', fg='#000')
        ###
        elif week > 1 and day == 1:
            weeks.config(text=f'{week} weeks and {day} day.', fg='#000')
        else:
            weeks.config(text=f'{week} weeks and {day} days.', fg='#000')

    except ValueError:
        weeks.config(text='Enter an integer number!', fg='red')


# --------------- BUTTONS & LABEL FOR PASSWORD ---------------
button = Button(frame, text='Calculate', bg='#303F9F', fg='#fff', height=2, font=3, command=passenger_week)
button.grid(row=3, columnspan=3, sticky='snew', padx=4, pady=20)

weekLabel = Label(frame, text='Number Of Weeks: ', bg='#E8EAF6', font=('time', 14, 'bold'))
weekLabel.grid(row=2, column=0, padx=4, pady=20)
weeks = Label(frame, text='', width=25, bg='#fff', font=('time', 13))
weeks.grid(row=2, column=1, columnspan=2, padx=4, pady=20, ipady=4)

root.mainloop()
