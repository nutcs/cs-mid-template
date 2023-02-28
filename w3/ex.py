from tkinter import *
from tkinter import messagebox

def mainwindow() :
   root = Tk()
   root.title("Week3-Lecture: Design layout using Frame by Nutthapon Salangsing")
   root.geometry("600x500")
   root.configure(bg='lightgreen')
   root.rowconfigure(0,weight=1)
   root.rowconfigure(1,weight=4)
   root.columnconfigure(0,weight=1)
   root.columnconfigure(1,weight=4)
   return(root)

def layout(root) : 
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
    right.columnconfigure(0,weight=1)
    return(top,left,right)

def topwidget(top) :
    bt1 = Button(top, text = "Click me1",image=img1,compound="top")
    bt1.grid(row=0,column=0,ipadx=30)
    bt2 = Button(top, text = "Exit Program",image=img2,compound="top")
    bt2.grid(row=0,column=1,ipadx=30)

def leftwidget(left) :
    book1 = Label(left,image=bk1,bg="#B9F3FC")
    book1.grid(row=0)
    book2 = Label(left,image=bk2,bg="#B9F3FC")
    book2.grid(row=1)
    book3 = Label(left,image=bk3,bg="#B9F3FC")
    book3.grid(row=2)

def rightwidget(right) :
    button1 = Button(right,text="Select Book1",command=clickbook1)
    button1.grid(row=0,ipadx=30,ipady=10)
    button2 = Button(right,text="Select Book2",command=clickbook2)
    button2.grid(row=1,ipadx=30,ipady=10)
    button3 = Button(right,text="Select Book3",command=clickbook3)
    button3.grid(row=2,ipadx=30,ipady=10)

def clickbook1() :
    messagebox.showinfo("Nutthapon said:","You select Book1")

def clickbook2() :
    messagebox.showinfo("Nutthapon said:","You select Book2")

def clickbook3() :
    messagebox.showinfo("Nutthapon said:","You select Book3")

root = mainwindow()
img1 = PhotoImage(file="w3/img/image/icon1.png")
img2 = PhotoImage(file="w3/img/image/icon2.png")
bk1 = PhotoImage(file="w3/img/image/book1.png")
bk2 = PhotoImage(file="w3/img/image/book2.png")
bk3 = PhotoImage(file="w3/img/image/book3.png")
top,left,right=layout(root)
topwidget(top)
leftwidget(left)
rightwidget(right)
root.mainloop()