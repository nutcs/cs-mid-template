from tkinter import *
def mainwindow() :
    root = Tk()
    root.title("GUI3: Class Activity of Week4 created by (type your english Nutthapon Salangsing)")
    root.geometry("600x600")
    root.configure(bg='lightgreen')
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=4)
    return(root)
def layout(root) :
    top = Frame(root,bg="#DBA39A")
    top.grid(row=0,columnspan=2,sticky='news')
    top.grid_columnconfigure((0,1),weight=1)
    top.grid_rowconfigure(0,weight=1)
    left = Frame(root,bg="#F5EBE0")
    left.grid(row=1,column=0,sticky='news')
    left.grid_rowconfigure((0,1,2),weight=1)
    left.grid_columnconfigure(0,weight=1)
    right = Frame(root,bg="#F0DBDB")
    right.grid(row=1,column=1,sticky='news')
    right.grid_rowconfigure((0,1,2),weight=1)
    right.grid_columnconfigure((0,1),weight=1)
    bottom = Frame(root,bg="#DBA39A")
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(top,left,right,bottom)
def topside(top) :
    bt1 = Button(top,text=" Click Me1 ",image=img1,compound=TOP)
    bt1.grid(row=0,column=0,ipadx=30)
    bt2 = Button(top,text="Exit Program",image=img2,compound=TOP,command=quit)
    bt2.grid(row=0,column=1,ipadx=30)
    
def bottomside(bottom) :
    showtotal = Label(bottom,fg='blue',font=("Comic Sans MS",24,"bold"),bg="#DBA39A")
    showtotal.pack(pady=10)
    return(showtotal)
def leftside(left) :
    product1 = Label(left,image=pro1,bg="#F5EBE0")
    product1.grid(row=0)
    product2 = Label(left,image=pro2,bg="#F5EBE0")
    product2.grid(row=1)
    product3 = Label(left,image=pro3,bg="#F5EBE0")
    product3.grid(row=2)
def rightside(right) :
    ck1 = Checkbutton(right,text="Product1 price = 100 baht",bg="#F0DBDB",variable=spy1,command=userClick)
    ck1.grid(row=0)
    ck2 = Checkbutton(right,text="Product1 price = 250 baht",bg="#F0DBDB",variable=spy2,command=userClick)
    ck2.grid(row=1)
    ck3 = Checkbutton(right,text="Product1 price = 150 baht",bg="#F0DBDB",variable=spy3,command=userClick)
    ck3.grid(row=2)

def userClick():
    global total
    total = 0
    if spy1.get() == 1:
        total += 100
    if spy2.get() == 1:
        total += 250
    if spy3.get():
        total += 150
    #print("Total price =",total)
    showtotal['bg'] = "#ffcefe"
    showtotal['fg'] = '#a75d5d'
    showtotal['text'] = 'Total price = ' + str(total) + 'bahts'

root = mainwindow()
spy1,spy2,spy3 = IntVar(),IntVar(),IntVar()
total = 0

top,left,right,bottom = layout(root)
img1 = PhotoImage(file="w4/image/icon1.png")
img2 = PhotoImage(file="w4/image/icon2.png")
pro1 = PhotoImage(file="w4/image/book1.png")
pro2 = PhotoImage(file="w4/image/book2.png")
pro3 = PhotoImage(file="w4/image/book3.png")

topside(top)
showtotal = bottomside(bottom)
leftside(left)
rightside(right)


root.mainloop()