# Importing Tkinter Module
from tkinter import *

# Create GUI Application Main Window
window = Tk()

# Adding Widgets And Configure Window
window.geometry("512x512")
window.title("KV Login Application")

# Code Of Button
def buttonClick():
    print(username.get())
    print(password.get())

# Creating Variable
username = StringVar()
password = StringVar()

# Implementing Frames In Tkinter
usernameContainer = Frame(window)
Label(usernameContainer,text="Username",padx=10,pady=10).pack(side="left")
Entry(usernameContainer).pack(side="left")
usernameContainer.pack()

passwordContainer = Frame(window)
Label(passwordContainer,text="Password ",padx=10,pady=10).pack(side="left")
Entry(passwordContainer,show="*").pack(side="left")
passwordContainer.pack()

Button(text="Submit",background="black",foreground="white",font="lucida 10 bold",command=buttonClick).pack()

# Enter The Main Event Loop To Take Action Against Each Event Triggered By The User
window.mainloop()