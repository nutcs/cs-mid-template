from tkinter import *

# bg
bgleft = '#FDA769'
bgright = '#F1F7B5'
bgcheckout = "#E8F3D6"
# bg

def window():
    root = Tk()
    root.geometry("600x600")
    root.option_add('*font','garamond 14')
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=5)
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure(1,weight=5)
    return root

def layout():
    top.grid(row=0,columnspan=2,sticky="news")
    top.columnconfigure((0,1,2),weight=1)
    top.rowconfigure(0,weight=1)

    bottom.grid(row=2,columnspan=2,sticky="news")
    bottom.columnconfigure((0,1),weight=1)
    bottom.rowconfigure(0,weight=1)

    left.grid(row=1,column=0,sticky="news")
    left.columnconfigure(0,weight=1)
    left.rowconfigure((0,1,2),weight=1)

    right.grid(row=1,column=1,sticky="news")
    right.rowconfigure((0,1,2),weight=1)
    right.columnconfigure((0,1),weight=1)

def topside():
    Button(top,text="cake",image=b1,compound=TOP,bg="#FDD36A",command=cakeClick).grid(row=0,column=0,sticky="news")
    Button(top,text="drink",image=b2,compound=TOP,bg="#FDD36A",command=drinkClick).grid(row=0,column=1,sticky="news")
    Button(top,text="check out",image=b3,compound=TOP,bg="#FDD36A",command=checkoutClick).grid(row=0,column=2,sticky="news")

def bottomside():
    Button(bottom,text="reset",bg="#4E6E81",fg="#fff").grid(row=0,column=0,sticky="news")
    Button(bottom,text="Exit",bg="#4E6E81",fg="#fff",image=b4,compound=LEFT,command=quit).grid(row=0,column=1,sticky="news")

def cakeClick():
    checkout.grid_forget()
    layout()
    for i,content in enumerate(nameCake):
        #left
        Label(left,text=content,image=imgCake[i],compound=BOTTOM,bg=bgleft).grid(row=i,ipadx=10,ipady=10)
        #right
        Label(right,text=cakePrice[i],bg=bgright).grid(row=i,column=0)
        Spinbox(right,from_=0,to=100,justify="center",width=20,textvariable=amtCake[i]).grid(row=i,column=1)

def drinkClick():
    checkout.grid_forget()
    layout()
    for i,content in enumerate(nameDrink):
        #left
        Label(left,text=content,image=imgDrink[i],compound=BOTTOM,bg=bgleft).grid(row=i,ipadx=10,ipady=10)
        #right
        Label(right,text=drinkPrice[i],bg=bgright).grid(row=i,column=0)
        Spinbox(right,from_=0,to=100,justify="center",width=20,textvariable=amtDrink[i]).grid(row=i,column=1)

def checkoutClick():
    # ลบ grid left,right
    left.grid_forget()
    right.grid_forget()
    # สร้าง Frameใหม่
    checkout.grid(row=1,columnspan=2,sticky="news")
    checkout.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    checkout.columnconfigure(0,weight=1)
    Label(checkout,text="- Summary of Cakes/Drink -",bg=bgcheckout,font=("Comic Sans MS", 22 ,"bold"),fg="blue").grid(row=2)
    #คำนวณราคา Cake และ Drink
    sumCake = 0
    sumDrink = 0
    for i in range(len(priceCake)):
        sumCake += amtCake[i].get() * priceCake[i]
        sumDrink += amtDrink[i].get() * priceDrink[i]
    
    totalcake = StringVar()
    Label(checkout,bg="#FFADBC",textvariable=totalcake).grid(row=3,sticky="news")
    totalcake.set("Total cake price %.2f"%sumCake)

    totalDrink = StringVar()
    Label(checkout,bg="#46C2CB",textvariable=totalDrink).grid(row=4,sticky="news")
    totalDrink.set("Total drink price %.2f"%sumDrink)

    priceAll = StringVar()
    Label(checkout,bg=bgcheckout,font=("Comic Sans MS", 22 ,"bold"),fg="blue",textvariable=priceAll).grid(row=5)
    priceAll.set("Total price = %.2f Baths"%(sumCake+sumDrink))




root = window()
b1 = PhotoImage(file="image/cake-button.png")
b2 = PhotoImage(file="image/drink-button.png")
b3 = PhotoImage(file="image/checkout.png")
b4 = PhotoImage(file="image/exit.png")

img1 = PhotoImage(file="image/drink1.png")
img2 = PhotoImage(file="image/drink2.png")
img3 = PhotoImage(file="image/drink3.png")
img4 = PhotoImage(file="image/cake3.png")
img5 = PhotoImage(file="image/cake2.png")
img6 = PhotoImage(file="image/cake4.png")
imgDrink = [img1,img2,img3]
imgCake = [img4,img5,img6]

nameCake = [' Strawberry Cake '," Cheese   Cake  ","Newyork Cheese Cake"]
nameDrink = ['| Orange   Mixed |',' Lemonade Mixed ',"| Mojito  Miexd  Berry |"]
cakePrice = ['(Price : 145) Amount:','(Price : 120) Amount:','(Price : 130) Amount:']
drinkPrice = ['(Price : 120) Amount:','(Price : 100) Amount:','(Price : 90) Amount:']

amtCake = [IntVar() for i in nameCake]
amtDrink = [IntVar() for i in nameDrink]

priceCake = [145,120,130]
priceDrink = [120,100,90]

top = Frame(root)
bottom = Frame(root)
left = Frame(root,bg=bgleft)
right = Frame(root,bg=bgright)
checkout = Frame(root,bg=bgcheckout)



layout()
topside()
bottomside()
root.mainloop()