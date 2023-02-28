from tkinter import *

def window():
    root = Tk()
    root.geometry("700x500")
    root.configure(bg="#FB2576")
    root.title("week6 : Menu widget By Nutthapon Salangsing")
    return root

def menu():
    bgs = "#FB2576"
    nameCake = (
        "Stawberry Cake\nPrice : 85",
        "Cheese Cake\nPrice : 95",
        "DIY Cake\nPrice : 100"
        )
    nameDrink = (
        "Strawberry Mixed\nPrice : 120",
        "Orange Mixed\nPrice : 140",
        "Coffee\nPrice : 80"
    )

    frame1 = Frame(root,bg='#FB2576')
    frame1.place(x=0,y=0,width=700,height=500)

    frame1.rowconfigure((0,4),weight=1)
    frame1.rowconfigure((1,2,3),weight=3)
    frame1.columnconfigure((0,1),weight=1)

    list_imgCake = (cakeImg1,cakeImg2,cakeImg3)
    list_imgDrink = (drinkImg1,drinkImg2,drinkImg3)

    for i in range(len(nameCake)):
        #Cake
        Label(frame1,text=nameCake[i],bg=bgs,fg="#fff",font="sans 13 bold").grid(row=i+1,column=0,sticky=NW,padx=50,pady=20)
        Spinbox(frame1,from_=0,to=100,justify="center",textvariable=amt[i]).grid(row=i+1,column=0,sticky=SW,padx=50,pady=30)
        Label(frame1,image=list_imgCake[i],bg=bgs).grid(row=i+1,column=0,sticky=NE,padx=50,pady=20)

        #Drink
        Label(frame1,text=nameDrink[i],bg=bgs,fg="#fff",font="sans 13 bold").grid(row=i+1,column=1,sticky=NW,padx=50,pady=20)
        Spinbox(frame1,from_=0,to=100,justify="center",textvariable=amt[i+3]).grid(row=i+1,column=1,sticky=SW,padx=50,pady=30)
        Label(frame1,image=list_imgDrink[i],bg=bgs).grid(row=i+1,column=1,sticky=NE,padx=70,pady=20)

def createmenu(root) :
    menubar = Menu(root)
    menubar.add_command(label="Product Menu",command=menu)
    menubar.add_command(label="Check out",command=checkList)
    menubar.add_command(label="Exit Program",command=root.quit)
    root.configure(bg="#FB2576",menu=menubar)

def checkList():
    bgs = "#609EA2"
    fgs = "#fff"
    Price = [85,95,100,120,140,80]
    header_check = ("Menu List","Amount","Price","Total(Bahts)")
    total = 0

    Frame2 = Frame(root,bg="#609EA2")
    Frame2.place(x=0,y=0,width=700,height=500)
    
    Frame2.rowconfigure((0,8),weight=2)
    Frame2.rowconfigure((1,2,3,4,5,6,7),weight=1)
    Frame2.rowconfigure((9),weight=3)

    Frame2.columnconfigure((0),weight=2)
    Frame2.columnconfigure((1,2,3),weight=1)
    for i,head in enumerate(header_check):
        Label(Frame2,text=head,font="15",bg=bgs,fg=fgs).grid(row=0,column=i)
    
    for i,n in enumerate(list_names):
        Label(Frame2,text=n,font="15",bg=bgs,fg=fgs).grid(row=i+1,sticky=E)
        Label(Frame2,text=str(amt[i].get()),font="15",bg=bgs,fg=fgs).grid(row=i+1,column=1)
        Label(Frame2,text=str(Price[i]),font="15",bg=bgs,fg=fgs).grid(row=i+1,column=2)
        Label(Frame2,text=str(amt[i].get() * Price[i]),font="15",bg=bgs,fg=fgs).grid(row=i+1,column=3)
        total += amt[i].get() * Price[i]
    
    # จนปัญญา ไม่สามารถเปลี่ยน Totals['text'] แบบไม่ใช้ฟังชั่นซ้อนกันได้
    def vat10():
        global vat
        if checkVat.get() == 1:
            vat = 0.1
            Totals['text'] = "Total price = %.2f"%(total + (total * vat))
        elif checkVat.get() == 0 :
            vat = 0
            Totals['text'] = "Total price = %.2f"%(total + (total * vat))

    Totals = Label(Frame2,text="Total price = %.2f"%(total + (total * vat)),font="bold",bg=bgs,fg=fgs)
    Totals.grid(row=9,columnspan=4)

    bgDiscount = Frame(Frame2,bg="#F6E6C2")
    bgDiscount.grid(row=8,columnspan=4,sticky="news")
    bgDiscount.rowconfigure(0,weight=1)
    bgDiscount.columnconfigure(0,weight=1)
    word="HAVE A MEMBER : (Click) YES (Discount 10%) or (Blank) NOT A MEMBER"
    Discount = Checkbutton(bgDiscount,text=word,variable=checkVat,bg="#F6E6C2",command=vat10)
    Discount.grid(row=0)

root = window()
cakeImg1 = PhotoImage(file="images/cake1.png")
cakeImg2 = PhotoImage(file="images/cake2.png")
cakeImg3 = PhotoImage(file="images/cake3.png")

drinkImg1 = PhotoImage(file="images/coffee1.png")
drinkImg2 = PhotoImage(file="images/coffee2.png")
drinkImg3 = PhotoImage(file="images/coffee3.png")

list_names = (
        "Stawberry Cake", "Cheese Cake",
        "DIY Cake", "Strawberry Mixed",
        "Orange", "Coffee"
)
amt = [IntVar() for i in list_names]
checkVat = IntVar()
vat = 0

createmenu(root)
root.mainloop()