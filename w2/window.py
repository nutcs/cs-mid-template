from tkinter import *

window = Tk()
def mainWindow():
    window.title("โปรแกรมพนันออนไลน์")
    window.geometry("500x500")
    window.configure(bg="#DA5235")

def write():
    name = Label(window,text="nutthapon",anchor="center",bg="#DA5235",fg="#fff")
    nickName = Label(window,text="nut",fg='#fff')
    name.pack()
    nickName.pack()

def end():
    window.mainloop()

mainWindow()
write()
end()

    