# Importing Tkinter Module
from tkinter import *

# Create GUI Application Main Window
window = Tk()

# Adding Widgets And Configure Window
window.geometry("512x512")
window.title("KV Button Application")

# Code Of Button
def buttonClick():
    print(username.get())

# Creating Variable
username = StringVar()

# Creating Label
Label(text="Username").pack()
# Creating Entry
Entry(textvariable=username).pack()
Button(text="Submit",background="black",foreground="white",font="lucida 10 bold",command=buttonClick).pack()

# Enter The Main Event Loop To Take Action Against Each Event Triggered By The User
window.mainloop()