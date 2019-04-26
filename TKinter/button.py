# Importing Tkinter Module
from tkinter import *

# Create GUI Application Main Window
window = Tk()

# Adding Widgets And Configure Window
window.geometry("512x512")
window.title("KV Button Application")

# Code Of Button
def buttonClick():
    print("Yeah.... You Have Clicked Me....")

Button(text="Magic",background="black",foreground="white",font="lucida 10 bold",command=buttonClick).pack()

# Enter The Main Event Loop To Take Action Against Each Event Triggered By The User
window.mainloop()