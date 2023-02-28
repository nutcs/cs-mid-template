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

def Exit(out):
    getOut = Button(out,text="Exit Program", font="Garamond 12 bold",command=quit,bd=5)
    getOut.grid(column=1,sticky=E,padx=30,ipady=10,ipadx=10)



root = window()
header,content,out,total = layout(root)


head(header)
Exit(out)

root.mainloop()