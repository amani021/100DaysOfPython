# -------- DAY 15 "ATM" --------
# Goal: Make an ATM that has 3 services:
#     - Balance Inquiries Service.
#     - Cash Withdrawal Service.
#     - Deposit Cash Service.
from tkinter import *

root = Tk()

root.title('100 Days Of Python - Day 15')
root.configure(background='#263238')
root.geometry('600x580')

# --------------- CREATE A FRAME ---------------
frame = LabelFrame(root, bg='#B0BEC5', padx=90, pady=79)
frame.pack(padx=20, pady=25)

infoLabel1 = Label(frame, text='Welcome to iPython ATM\n', bg='#B0BEC5', font=('time', 21, 'bold'))
infoLabel1.grid(row=0, column=0, columnspan=2, padx=4)
infoLabel2 = Label(frame, text='Please enter your username & password\n\n', bg='#B0BEC5', font=('time', 14))
infoLabel2.grid(row=1, column=0, columnspan=2, padx=4, pady=18)

# 2 fields for username and password
username = Label(frame, text='Username: ', bg='#B0BEC5', font=('time', 14, 'bold'))
username.grid(row=2, column=0, pady=3)
e_name = Entry(frame, width=21, font=3)
e_name.grid(row=2, column=1, pady=3)
password = Label(frame, text='Password: ', bg='#B0BEC5', font=('time', 14, 'bold'))
password.grid(row=3, column=0, pady=3)
e_pwd = Entry(frame, width=21, font=3)
e_pwd.grid(row=3, column=1, pady=3)


# --------------- CLASS ---------------
class AtmServices:
    global balance
    balance = 5400
    # Services options
    services = [
        ('Balance Inquiries', 'Inquiries'),
        ('Cash Withdrawal', 'Cash'),
        ('Deposit Cash', 'Deposit')
    ]
    # Balance Options
    money = [(5000, 5000), (3000, 3000), (1500, 1500)]
    serv = StringVar()
    serv.set('Inquiries')
    val = IntVar()
    val.set(5000)

    # Constructor method
    def __init__(self, name):
        self.name = name

    # --------------- METHODS ---------------
    # Balance Inquiries - الاستفسار عن الرصيد
    def inquiries(self):
        global result_label1
        infoLabel2.config(text='Balance Inquiries Service\n')
        # Display the balance that he has in his account
        result_label1 = Label(frame, text=f'Your current balance equals {balance}$', width=28, height=6, bg='#B0BEC5',
                              font=('time', 16))
        result_label1.grid(row=2, column=0, rowspan=3, columnspan=2, padx=12, pady=18)
        next_btn.config(text='Back', command=lambda: self.result(1, 1))

    # Cash Withdrawal - سحب نقدي
    def cash(self):
        infoLabel2.config(text='How much do you want?\n')
        i, number = 1, 0
        # Loop for display the balance options
        for value, num in self.money:
            i += 1
            Radiobutton(frame, text=f'  {value}$ .', variable=self.val, value=num, bg='#B0BEC5', width=28,
                        height=2, font=15).grid(row=i, column=0, columnspan=2, padx=12, pady=2)
        next_btn.config(command=lambda: self.result(2, self.val.get()))

    # Deposit Cash - إيداع نقدي
    def deposit(self):
        global question, e_num, label
        infoLabel2.config(text='Deposit Cash Service')
        label = Label(frame, height=11, width=45, bg='#B0BEC5')
        label.grid(row=2, column=0, rowspan=3, columnspan=2)
        # Field to write the number of money that will deposit
        question = Label(frame, text='How much do you want to deposit?\n', height=4, bg='#B0BEC5', font=('time', 14, 'bold'))
        question.grid(row=2, column=0, rowspan=2, columnspan=2, pady=7)
        e_num = Entry(frame, width=18, font=3)
        e_num.grid(row=3, column=0, columnspan=2, pady=3)
        next_btn.config(command=lambda: self.result(3, 0))

    # Output will display depending on the choice of service
    def result(self, val, number):
        # If the user choice the first service (Balance Inquiries)
        if val == 1:
            self.create_button(number)
        # If the user choice the second service (Cash Withdrawal)
        elif val == 2:
            global result_label2
            infoLabel2.config(text='Cash Withdrawal Service\n')
            # Display the balance after
            result_label2 = Label(frame, text=f'An amount of {number}$ has been withdrawn.\nYour balance is now '
                                              f'{balance - number}$', width=32, height=6, bg='#B0BEC5',
                                  font=('time', 16))
            result_label2.grid(row=2, column=0, rowspan=3, columnspan=2, padx=12, pady=18)
            next_btn.config(text='Back', command=lambda: self.clear(2))
        # If the user choice the third service (Deposit Cash)
        elif val == 3:
            global result_label3
            infoLabel2.config(text='Deposit Cash Service\n')
            question.config(text='')
            # Display the balance after adding some money to the account
            result_label3 = Label(frame, text=f'An amount of {e_num.get()}$ has been deposit\ninto your account.\n\n'
                                              f'Your balance is now {balance + int(e_num.get())}$', width=32,
                                  bg='#B0BEC5', font=('time', 16))
            result_label3.grid(row=2, column=0, rowspan=3, columnspan=2, padx=12, pady=4)
            next_btn.config(text='Back', command=lambda: self.clear(3))

    def clicked(self, code):
        if code == 'Inquiries':
            self.inquiries()
        elif code == 'Cash':
            self.cash()
        elif code == 'Deposit':
            self.deposit()

    # Method for exit from the ATM
    def exit(self):
        infoLabel1.config(text='Thanks ..')
        exit_label = Label(frame, height=80, width=50, bg='#B0BEC5')
        exit_label.grid(row=1, column=0, rowspan=5, columnspan=2)

    # Create the second screen which has services options
    def create_button(self, code):
        if code == 0:
            self.clear(1)
        elif code == 1:
            pass
        infoLabel1.config(text=f'Welcome {self.name}')
        infoLabel2.config(text='Choose the required service\n')
        i = 1
        # Loop for display the services options
        for text, mode in self.services:
            i += 1
            Radiobutton(frame, text=f'  {text} Service.', variable=self.serv, value=mode, bg='#B0BEC5', width=28,
                        height=2, font=15).grid(row=i, column=0, columnspan=2, padx=12, pady=2)

        global next_btn, exit_btn
        # Create button for next step or can be for previous step
        next_btn = Button(frame, text='Next', bg='#78909C', width=12, height=2, font=14,
                          command=lambda: self.clicked(self.serv.get()))
        next_btn.grid(row=5, column=0, padx=1, pady=12)
        # Create button for exit from an ATM
        exit_btn = Button(frame, text='Exit', bg='#78909C', width=12, height=2, font=14,
                          command=lambda: self.exit())
        exit_btn.grid(row=5, column=1, padx=1, pady=12)

    # Clear some elements for some reason
    def clear(self, val):
        if val == 1:
            username.destroy()
            e_name.destroy()
            password.destroy()
            e_pwd.destroy()
            submit.destroy()
            errorLabel.config(text='')
        elif val == 2:
            result_label2.config(text='')
            self.result(1, 1)
        elif val == 3:
            result_label3.config(text='')
            self.result(1, 1)


# --------------- OUT OF CLASS ---------------
# Create an object for the class
user_account = AtmServices(e_name.get())


# --------------- FUNCTIONS ---------------
# Check if the user enter his username and password or not
def check():
    if e_name.get() == '' or e_pwd.get() == '':
        errorLabel.config(text='Empty Field(s)!!')
    else:
        user_account.create_button(0)


errorLabel = Label(frame, text='', bg='#B0BEC5', fg='red', font=('time', 16))
errorLabel.grid(row=4, column=0, columnspan=2, padx=12, pady=18)
submit = Button(frame, text='Log In', bg='#78909C', width=12, height=2, font=14, command=check)
submit.grid(row=5, column=0, columnspan=2, padx=12, pady=15)

root.mainloop()
