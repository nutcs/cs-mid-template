from tkinter import *


def Window():
    root = Tk()
    root.title("test")
    root.geometry("500x500")
    root.configure(bg="red")
    root.grid_columnconfigure((1,2),weight=1)
    root.option_add('*font','Garamond 16 bold')
    return root

root = Window()
root.mainloop()