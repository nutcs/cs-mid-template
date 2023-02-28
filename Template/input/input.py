from tkinter import *


def Window():
    root = Tk()
    root.title("test")
    root.geometry("500x500")
    root.configure(bg="red")
    root.grid_columnconfigure((0,1),weight=1)
    root.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
    root.option_add('*font','Garamond 16 bold')
    return root

def inputs_Radiobutton(root):
    Label(root,text="Radiobutton").grid(row=0,column=0)
    #Radio Buttonแสดงทางเลือกให้ผู้ใช้เลือกได้1ทางเลือก
    Radiobutton(root,text="Radiobutton1",bg='pink',variable=v,value=1).grid(row=1,column=0)
    Radiobutton(root,text="Radiobutton2",bg='pink',variable=v,value=2).grid(row=2,column=0)
    
def input_Checkbox(root):
    Label(root,text="Checkbutton").grid(row=3,column=0)
    #Checkboxแสดงทางเลือกให้ผู้ใช้เลือกได้หลายทางเลือก
    Checkbutton(text="Option1",bg='pink',variable=v1,command=check).grid(row=4,column=0)
    Checkbutton(text="Option2",bg='pink',variable=v2).grid(row=5,column=0)

def input_Scale(root):
    Label(root,text="Scale").grid(row=6,column=0)
    Scale(root,from_=0,to=100,orient='horizontal',bg='lightblue',length=300).grid(row=7,column=0)

def check():
    if v1.get():
        print(v1.get())
    else:
        print(v1.get())


root = Window()

#Radiobutton
v= IntVar()

#Checkbox
v1,v2= IntVar(),IntVar()






inputs_Radiobutton(root)
input_Checkbox(root)
input_Scale(root)
root.mainloop()