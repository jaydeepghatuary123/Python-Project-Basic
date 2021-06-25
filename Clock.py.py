from tkinter import *
from time import strftime

root=Tk()
root.title("Clock")

def time():
    string=strftime('%H:%M:%S %p')
    x.config(text=string)
    x.after(1000,time)


x=Label(root, font=("ds-digital",80) ,background="black",foreground="cyan")
x.pack()
time()
root.mainloop()
