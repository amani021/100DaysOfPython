# -------- DAY 11 "OOP" --------
# Goal: Use class to view images
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('100 Days Of Python - Day 11')
root.config(background='#BBDEFB')


class language:
    name, new_pyImage = [], 0
    lang = StringVar()
    lang.set('python')

    # Constructor function
    def __init__(self, name):
        self.name.append(name)

    def clicked(self, code):
        if code == 'Python':
            # Open Image
            pyImage = Image.open('image\Features-of-python.jpg')
            self.resizeImage(pyImage)
        elif code == 'C++':
            # Open Image
            cpImage = Image.open('image\Features-of-C++.jpg')
            self.resizeImage(cpImage)

    def create_button(self):
        for i in range(len(self.name)):
            Radiobutton(root, text=f'   {self.name[i]} Features', variable=self.lang, value=self.name[i], bg='#FFECB3', width=20, height=3, font=14, \
                command=lambda: self.clicked(self.lang.get())).grid(row=1, column=i, padx=12, pady=25)

    # Function for resize a dimention of an image
    def resizeImage(self, name_img):
        resized = name_img.resize((480, 260), Image.ANTIALIAS)
        self.new_pyImage = ImageTk.PhotoImage(resized)
        imgLabel = Label(root, image=self.new_pyImage)
        imgLabel.grid(row=2, column=0, columnspan=2, padx=20, pady=25)


# Create objects for class language
python = language('Python')
cPlus = language('C++')

# Use one of objects is enough; because both of them is a class's object
# python.create_button()
cPlus.create_button()

root.mainloop()
