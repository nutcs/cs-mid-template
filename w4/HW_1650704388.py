from tkinter import *

root = Tk()
def window():
    root.geometry("600x600")
    root.title("GUI3: Class Activity of Week4 created by Nutthapon Salangsing")
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=6)
    root.rowconfigure(2,weight=2)
    root.columnconfigure((0,1),weight=1)
    return root

def layout(root):
    header = Frame(root,bg="#d4a59c")
    header.grid(row=0,columnspan=2,sticky="news")
    header.grid_columnconfigure(0,weight=1)
    header.grid_rowconfigure(0,weight=1)

    content = Frame(root,bg="#f4ebe1")
    content.grid(row=1,column=0,sticky="news")
    content.grid_rowconfigure((0,1,2),weight=1)
    content.grid_columnconfigure((0,1),weight=1)
    
    total = Frame(root,bg="#ded0d0")
    total.grid(row=1,column=1,sticky="news")
    total.grid_rowconfigure((0,1,2),weight=1)
    total.grid_columnconfigure((0),weight=1)

    out = Frame(root,bg="#d4a59c")
    out.grid(row=2,columnspan=2,sticky="news")
    out.grid_columnconfigure((0,1),weight=1)
    out.grid_rowconfigure(0,weight=1)

    return header,content,out,total

def head(header):
    text = Label(header,text="My Cake Shop by Nutthapon",font='Tahoma 15 bold',bg="#d4a59c")
    text.grid(column=0,row=0)

def Img_menu(content):
    Cake1 = Label(content,image=Img_cake1,bg="#f4ebe1")
    Cake1.grid(row=0,column=0)
    
    Cake2 = Label(content,image=Img_cake2,bg="#f4ebe1")
    Cake2.grid(row=1,column=0)
    
    Cake3 = Label(content,image=Img_cake3,bg="#f4ebe1")
    Cake3.grid(row=2,column=0)

def menu(content):
    def userClick():
        c1 = int(prices1.get())
        c2 = int(prices2.get())
        c3 = int(prices3.get())

        total = (c1 * 160)+(c2 * 170)+(c3 * 45)
        sumPrice['text'] = str(total) , 'Bahts'
        
    Cake1 = Label(content,text="Chocolate Cake\nPrice 160 baths",font='Tahoma 11',bg="#f4ebe1")
    Cake1.grid(row=0,column=1,sticky=N,pady=30)
    #wrap="true",
    prices1 = Spinbox(content, state='readonly', from_=0, to=100, font="Garamond 14 bold",  command=userClick,justify="center")
    prices1.grid(row=0,column=1,sticky=S,pady=20)

    Cake2 = Label(content,text="Strawberry Cake\nPrice 170 baths",font='Tahoma 11',bg="#f4ebe1")
    Cake2.grid(row=1,column=1,sticky=N,pady=30)
    prices2 = Spinbox(content, state='readonly', from_=0, to=100, font="Garamond 14 bold", command=userClick,justify="center")
    prices2.grid(row=1,column=1,sticky=S,pady=20)

    Cake3 = Label(content,text="Donut Party\nPrice 45 baths",font='Tahoma 11',bg="#f4ebe1")
    Cake3.grid(row=2,column=1,sticky=N,pady=30)
    prices3 = Spinbox(content, state='readonly', from_=0, to=100, font="Garamond 14 bold", command=userClick,justify="center")
    prices3.grid(row=2,column=1,sticky=S,pady=20)

def price(total):
    text = Label(total,text="Thank You for your shopping\nTotal Price is",font='Tahoma 13 bold',bg="#ded0d0")
    text.grid(row=0)

    sumPrice = Label(total,text="0 Baths",fg="blue",font="Garamond 22 bold",bg="#ded0d0")
    sumPrice.grid(row=1)
    return sumPrice

def Exit(out):
    getOut = Button(out,text="Exit Program", font="Garamond 12 bold",command=quit,bd=5)
    getOut.grid(column=1,sticky=E,padx=30,ipady=10,ipadx=10)


Img_cake1 = PhotoImage(file="w4/image/cake1.png")
Img_cake2 = PhotoImage(file="w4/image/cake2.png")
Img_cake3 = PhotoImage(file="w4/image/cake3.png")

root = window()
spy1,spy2,spy3 = IntVar(),IntVar(),IntVar()
totals = 0

header,content,out,total = layout(root)
head(header)
Img_menu(content)
menu(content)
sumPrice = price(total)
Exit(out)


root.mainloop()