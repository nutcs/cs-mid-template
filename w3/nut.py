from tkinter import *

root = Tk()

def window():
    root.geometry("650x500")
    root.configure(bg='lightgreen')
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=4)

def layout() : 
    top = Frame(root,bg="#86C8BC")
    top.grid(row=0,columnspan=2,sticky="news")
    top.rowconfigure(0,weight=1)
    top.columnconfigure((0,1),weight=1)

    left = Frame(root,bg="#B9F3FC")
    left.grid(row=1,column=0,sticky="news")
    left.rowconfigure((0,1,2),weight=1)
    left.columnconfigure(0,weight=1)

    right = Frame(root,bg="#B6EADA")
    right.grid(row=1,column=1,sticky="news")
    right.rowconfigure((0,1,2),weight=1)
    right.columnconfigure((0,1,2),weight=1)
    return top,left,right

def header(top):
    bt1 = Button(top,text="click me",image=b1,compound="top")
    bt1.grid(row=0,column=0,ipadx=30)

    bt2 = Button(top,text="Exit Program",image=b2,compound="top")
    bt2.grid(row=0,column=1,ipadx=30)

def book(left):
    b1 = Label(left,image=book1)
    b1.grid(row=0)

    b2 = Label(left,image=book2)
    b2.grid(row=1)

    b3 = Label(left,image=book3)
    b3.grid(row=2)

def click(right):
    bt1 = Button(right,text="click 1")
    bt1.grid(row=0,column=1,ipadx=30,ipady=10)
    bt2 = Button(right,text="click 2")
    bt2.grid(row=1,column=1,ipadx=30,ipady=10)
    bt3 = Button(right,text="click 3")
    bt3.grid(row=2,column=1,ipadx=30,ipady=10)


#img
b1 = PhotoImage(file="w3/img/image/icon1.png")
b2 = PhotoImage(file="w3/img/image/icon2.png")

book1 = PhotoImage(file="w3/img/image/book1.png")
book2 = PhotoImage(file="w3/img/image/book2.png")
book3 = PhotoImage(file="w3/img/image/book3.png")

window()
top,left,right = layout()
header(top)
book(left)
click(right)

root.mainloop()