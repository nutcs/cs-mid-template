from tkinter import *

def Window():
    root = Tk()
    root.title("test")
    root.geometry("800x500")
    root.configure(bg="red")
    root.grid_rowconfigure((0),weight=1)
    root.grid_rowconfigure((1),weight=10)
    root.grid_columnconfigure((0,1),weight=1)
    root.option_add('*font','Garamond 16')
    return root

def tabMenu():
    top = Frame(root,bg="#F7C8E0")
    top.grid(row=0,columnspan=2,sticky="news")
    top.rowconfigure(0,weight=1)
    Button(top,text="Tool Bar1").grid(row=0,column=0,sticky=W,padx=10,ipadx=15)
    Button(top,text="Tool Bar2").grid(row=0,column=0,sticky=W,padx=160,ipadx=15)

def product_menu():
    left = Frame(root,bg="#B4E4FF")
    left.grid(row=1,column=0,sticky="news")
    left.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    left.columnconfigure((0,1),weight=1)

    Label(left,text="Product Summary :",bg="#B4E4FF").grid(row=0,column=0,sticky=NW)
    pos = 1
    for i,content in enumerate(text):
        Label(left,bg="#B4E4FF",image=cakeImg[i]).grid(rowspan=2,row=pos,column=0) # Img = row 1,2,3
        Label(left,text=content,bg="#B4E4FF").grid(row=pos,column=1,sticky=N) #row 1,3,5
        Spinbox(left,from_=0,to=100,width=15,justify="center").grid(row=pos+1,column=1,sticky=N) #row 2,4,6
        pos += 2


def product_summary():
    right = Frame(root,bg="#FDD36A")
    right.grid(row=1,column=1,sticky="news")
    right.rowconfigure((0,1,2,3,4),weight=1)
    right.rowconfigure(5,weight=8)
    right.columnconfigure((0,1),weight=1)

    Label(right,text="Product Summary :",bg="#FDD36A").grid(row=0,column=0,sticky=NW)
    for i,content in enumerate(text):
        Label(right,text=content,bg="#FDD36A").grid(row=i+1,column=0,sticky=NE) #row 1,2,3
        Entry(right,width=15,justify="center").grid(row=i+1,column=1,sticky=N) #row 1,2,3
    
    Label(right,text="Total Price :",bg="#FDD36A").grid(row=4,column=0,sticky=NE)
    Entry(right,width=15,justify="center").grid(row=4,column=1,sticky=N)



root = Window()
#price text
text = ["Product 1 : Wow1\nPrice 200 baths","Product 2 : Wow2\nPrice 300 baths","Product 3 : Wow3\nPrice 400 baths"]
cakeImg1 = PhotoImage(file="mid_w3/cake1.png")
cakeImg2 = PhotoImage(file="mid_w3/cake2.png")
cakeImg3 = PhotoImage(file="mid_w3/cake3.png")

cakeImg = [cakeImg1,cakeImg2,cakeImg3]


tabMenu()
product_menu()
product_summary()

root.mainloop()