from tkinter import *
from tkinter import messagebox 

#week3
def mainwindow() :
    root= Tk()
    root.title("GUI2: Design layout using Frame")
    root.geometry("600x500")
    root.configure(bg='lightgreen')
    root.rowconfigure((0,1,2),weight=2)
    root.columnconfigure(0,weight=1)
    return(root)
root= mainwindow()
messagebox.showinfo("Information","Hi, Sirinthorn Cheyasak")
messagebox.showwarning("Warning","Warning...")
messagebox.showerror("Error","Pleasetry again")
root.mainloop()