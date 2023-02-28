from tkinter import *

window = Tk()
def mainWindow():
    window.title("test")
    window.geometry("500x500")
    window.configure(bg="red")
    window.grid_columnconfigure((1,2),weight=1)
    window.option_add('*font','Garamond 16 bold')

def header():
    head = Label(window,text="djsgpjg",fg="#fff",bg="red")
    head.grid(row=0,columnspan=3,pady=20,sticky="new")

def text(index):
    bgs,color = "red","#fff"
    name = Label(text=names[index-2],bg=bgs,fg=color,font=(25))
    name.grid(row=index,column=1,sticky=E,padx=20)

    box = Entry()
    box.grid(row=index,column=2,sticky=W,padx=20)

def bt():
    cancel = Button(text="Cancel",bg="#fff",fg="black")
    cancel.grid(row=10,column=1,sticky=E,padx=20,pady=20)
    
    cance2 = Button(text="Register")
    cance2.grid(row=10,column=2,sticky=W,padx=20,pady=20)

names = ("Name :","Email :","Gender :","Phone number :","Phone number :","Phone number :","Phone number :","Phone number :")
for i in range(len(names)):
    text(i+2)

mainWindow()
header()
bt()
window.mainloop()
