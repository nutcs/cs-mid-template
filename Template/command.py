from tkinter import *


def Window():
    root = Tk()
    root.title("test")
    root.geometry("500x500")
    root.configure(bg="red")
    root.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    root.grid_columnconfigure((0,1),weight=1)
    root.option_add('*font','Garamond 16 bold')
    return root

def command():
    if(a1["text"] == "clicked"):
        a1["text"] = "text1"
    else:
        a1["text"] = "clicked"

def command2():
    a2["text"] = str(spy1.get())

def tools(root):
    Button(root,text="b1",width=10,command=command).grid(row=0,column=0)
    number1 = Spinbox(root,from_=0,to=100,justify="center",textvariable=spy1,width=10,command=command2)
    number1.grid(row=1,column=0)
    Button(root,text="b3",width=10).grid(row=2,column=0)


def text(root):
    a1 = Label(root,text="text1")
    a1.grid(row=0,column=1)

    a2 = Label(root,text="text2")
    a2.grid(row=1,column=1)
    
    a3 = Label(root,text="text3")
    a3.grid(row=2,column=1)

    return a1,a2,a3


root = Window()
spy1 = IntVar()

tools(root)
a1,a2,a3 = text(root)
root.mainloop()