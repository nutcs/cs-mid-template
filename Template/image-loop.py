from tkinter import *

def window():
    root = Tk()
    root.geometry("700x500")
    root.configure(bg="#FB2576")
    root.title("week6 : Menu widget By Nutthapon Salangsing")
    root.rowconfigure((0,4),weight=1)
    root.rowconfigure((1,2,3),weight=3)
    root.columnconfigure((0,1),weight=1)
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

    list_imgCake = (cakeImg1,cakeImg2,cakeImg3)
    list_imgDrink = (drinkImg1,drinkImg2,drinkImg3)

    for i in range(len(nameCake)):
        #Cake
        Label(root,text=nameCake[i],bg=bgs,fg="#fff",font="sans 13 bold").grid(row=i+1,column=0,sticky=NW,padx=50,pady=20)
        Spinbox(root,from_=0,to=100,justify="center").grid(row=i+1,column=0,sticky=SW,padx=50,pady=30)
        Label(root,image=list_imgCake[i],bg=bgs).grid(row=i+1,column=0,sticky=NE,padx=20,pady=20)

        #Drink
        Label(root,text=nameDrink[i],bg=bgs,fg="#fff",font="sans 13 bold").grid(row=i+1,column=1,sticky=NW,padx=50,pady=20)
        Spinbox(root,from_=0,to=100,justify="center").grid(row=i+1,column=1,sticky=SW,padx=50,pady=30)
        Label(root,image=list_imgDrink[i],bg=bgs).grid(row=i+1,column=1,sticky=NE,padx=70,pady=20)


root = window()
cakeImg1 = PhotoImage(file="Template/image/cake1.png")
cakeImg2 = PhotoImage(file="Template/image/cake2.png")
cakeImg3 = PhotoImage(file="Template/image/cake3.png")

drinkImg1 = PhotoImage(file="Template/image/coffee1.png")
drinkImg2 = PhotoImage(file="Template/image/coffee2.png")
drinkImg3 = PhotoImage(file="Template/image/coffee3.png")


menu()
root.mainloop()