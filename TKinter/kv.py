# Importing Library
from tkinter import *
import tkinter.messagebox as messagebox

# Making Main Window
root = Tk()
root.geometry("1024x500")
root.maxsize(1024,500)
root.minsize(1024,500)
root.title("KV Login System")
root.configure(background="white")
# Making Header Of Application
header = Frame(root)
Label(header,text="KV Login",font="lucida 30 bold italic",background="white",foreground="#1e90ff").pack(fill=X)
header.pack(fill=X)

# Adding Logo Of KV School
imageContainer = Frame(root,padx=100,background="white")
image = PhotoImage(file="kv.png")
Label(imageContainer,image=image,background="white").pack(anchor="center")
imageContainer.pack(anchor="center",side="left")

# Making Form Of Login
loginContainer = Frame(root,background="white",pady=100)
Label(text="Login",background="white",font="lucida 20 bold" ,foreground="#1e90ff").pack()

# Making Two Variables That Store Username And Password 
username = StringVar()
password = StringVar()
# Making Container For The Username
usernameContainer = Frame(loginContainer,padx=100,background="white")
Label(usernameContainer,text="Enter Your Username",background="white",font="lucida 10 bold",padx=20,pady=10).pack(side="left")
usernameEntry = Entry(usernameContainer,textvariable=username)
usernameEntry.pack(side="left")
usernameContainer.pack()

# Making Container For The Password
passwordContainer = Frame(loginContainer,padx=100,background="white")
Label(passwordContainer,text="Enter Your Username",background="white",font="lucida 10 bold",padx=20,pady=10).pack(side="left")
passwordEntry = Entry(passwordContainer,show="*",textvariable=password)
passwordEntry.pack(side="left")
passwordContainer.pack()

# Clear And Focus Function
def utilityFunction():
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    usernameEntry.focus()

# Login Function
def login():
    # print(username.get())
    # print(password.get())
    if username.get() == "kv" and password.get() == "kvpassword":
        messagebox.showinfo(title="KV Login",message="You Have Login Successfully")
        utilityFunction()
        
    else:
        messagebox.showerror(title="KV Login",message="You Have Entered Wrong Password")
        utilityFunction()

# Button In LoginContainer
Button(loginContainer,text="submit",background="white",font="bold",command=login).pack()
loginContainer.pack(side="top",anchor="w")
root.mainloop()