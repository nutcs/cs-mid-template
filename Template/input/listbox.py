from tkinter import*
from tkinter import ttk
#week 4
root= Tk()
root.geometry("500x200")
root.title("Common widget: Listbox Widget")
root.configure(bg="pink")
combo= ttk.Combobox(root,values=["Java","C#","Swift","Python","PHP","NodeJS"])
combo.set("Python")
combo.pack(pady=20)
root.mainloop()