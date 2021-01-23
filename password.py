import random
import pyperclip
from tkinter import * 
from tkinter.ttk import *
import string

def low():
    entry.delete(0, END)

    length = var1.get()

    #lower = random.choice(string.ascii_letters)[0].lower()
    # lower = string.ascii_letters[0:26]
    # upper = string.ascii_letters
    # punctuation = string.punctuation
    # digits = list(range(0,10))
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password

    # elif var.get() == 4:
    #     for i in range(0, length):
    #         password = password + random.choice(punctuation)
    #     return password
    else:
        print("Please choose an option")

def generate():
    password1 = low()
    entry.insert(10, password1)

def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Cryofracture's Random Password Generator")

Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

c_label = Label(root, text="Length")
c_label.grid(row=1)

copy_button = Button(root, text="Copy to clipboard", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate Password", command=generate)
generate_button.grid(row=0,column=3)

radio_low = Radiobutton(root, text="Low strength", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium strength", variable=var, value=0)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="High strength", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')
# radio_max = Radiobutton(root, text="Max strength", variable=var, value=4)
# radio_max.grid(row=1, column=5, sticky='E')
combo = Combobox(root, textvariable=var1)

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)

combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

root.mainloop()