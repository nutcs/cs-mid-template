from tkinter import *
from tkinter import messagebox

root = Tk()

def window():
    root.geometry("650x500")
    root.title("Dashbroad by Nutthapon Salangsing")
    root.configure(bg='#fff')
    root.option_add('*font','Garamond 18 bold')
    root.rowconfigure(1,weight=4)
    root.rowconfigure(2,weight=2)
    root.columnconfigure(0,weight=1)

def layout():
    header = Frame(root,bg="#fff")
    header.grid(row=0,column=0,sticky="news")
    header.rowconfigure(0,weight=1)
    header.columnconfigure(0,weight=1)

    profile = Frame(root)
    profile.grid(row=1,column=0,sticky="news")
    profile.columnconfigure(0,weight=2)
    profile.rowconfigure((0),weight=1)

    tabProfile = Frame(profile,bg="#fff3cd")
    tabProfile.grid(row=0,column=0,sticky="news")
    tabProfile.rowconfigure((0),weight=1)
    tabProfile.columnconfigure((0),weight=1)

    tabSkill = Frame(profile,bg='#cce5ff')
    tabSkill.grid(row=0,column=1,sticky="news")
    tabSkill.rowconfigure((0,1,2),weight=1)

    run = Frame(root,bg="#4bacc6")
    run.grid(row=2,column=0,sticky="news")
    run.columnconfigure((0,1,2,3),weight=1)
    run.rowconfigure(0,weight=1)
    return header,tabProfile,tabSkill,run

def head(header):
    text = Label(header,text="Dashbroad by Nutthapon Salangsing",bg="#d1e4fd",font=14)
    text.grid(row=0,column=0,ipady=10,pady=10,ipadx=140)

def Profile(p):
    tab = Frame(p,bg="#fff")
    tab.grid(row=0,column=0,sticky="news",padx=15,pady=15)
    tab.rowconfigure((0),weight=3)
    #tab.rowconfigure((1),weight=1)
    tab.columnconfigure((0),weight=1)

    tab2 = Frame(tab,bg="#fff")
    tab2.grid(row=1,column=0,sticky="news")
    tab2.columnconfigure((0,1,2,3),weight=1)

    data1 = Label(tab2,text="27\nAge",bg="#53a551",fg="#fff",width=12)
    data1.grid(row=0,column=0,ipady=10,sticky=SW,pady=10)
    
    data2 = Label(tab2,text="55\nWeight",bg="#ffc107",fg="#fff",width=12)
    data2.grid(row=0,column=1,ipady=10,sticky=SW,pady=10)
    
    data3 = Label(tab2,text="165\nHeight",bg="#17a2b8",fg="#fff",width=12)
    data3.grid(row=0,column=2,ipady=10,sticky=SW,pady=10)
    
    data4 = Label(tab2,text="5\nSkill",bg="#dc3545",fg="#fff",width=12)
    data4.grid(row=0,column=3,ipady=10,sticky=SW,pady=10)
    return tab

def mainProfile(tab):
    key = """
    Intructor
    Information Technology and Innovation
    \n\n\n
    """
    text = Label(tab,text=key,font='Garamond 9 bold',bg="#fff")
    text.grid(row=0,sticky=SE,padx=25)#sticky=SE,ipadx=0,ipady=0,padx=25,pady=140

    texthead = Label(tab,text="Miss Nutthapon Salangsing",font='Garamond 14 bold',bg="#fff")
    texthead.grid(row=0,column=0,sticky=E,padx=20)

    me = Label(tab,image=img_profile,bg="#fff")
    me.grid(row=0,column=0,sticky=W,padx=5)



def skill(tabSkill):
    tab = Frame(tabSkill,bg="#fff")
    tab.grid(row=1,column=0,padx=15,sticky="news",ipadx=10,ipady=70)
    tab.rowconfigure((0,1),weight=1)
    tab.columnconfigure(0,weight=1)

    text =Label(tab,text="My English Skill",bg="#fff",fg="blue",font=18)
    text.grid(row=0,column=0,ipady=0,sticky=SW,padx=5,pady=0)

    doc = Label(tab,bg="#fff",image=img_skill,compound="bottom")
    doc.grid(row=1,column=0,ipadx=0,ipady=0,padx=0)

def button(run):
    bt1 = Button(run,text="Click me1",bg="#f1c297",command=clickme1)
    bt1.grid(row=0,column=0)

    bt2 = Button(run,text="Click me2",bg="#f1c297",command=clickme2)
    bt2.grid(row=0,column=1)

    bt3 = Button(run,text="Click me3",bg="#f1c297",command=clickme3)
    bt3.grid(row=0,column=2)
    
    bt4 = Button(run,text="Exit Program",bg="#f1c297",command=root.destroy)
    bt4.grid(row=0,column=3)

def clickme1():
    messagebox.showinfo("Nutthapon said:","click me1 clicked")
def clickme2():
    messagebox.showinfo("Nutthapon said:","click me2 clicked")
def clickme3():
    messagebox.showinfo("Nutthapon said:","click me3 clicked")



# img
img_skill = PhotoImage(file="w3/homeWork/hw3-images/skill.png").subsample(2,2)
img_profile = PhotoImage(file="w3/homeWork/hw3-images/female.png").subsample(4,4)

a = ['#cce5ff',"#fff3cd","#4bacc6"]
window()
header,tabProfile,tabSkill,run = layout()
head(header)
tab = Profile(tabProfile)
mainProfile(tab)
skill(tabSkill)
button(run)
root.mainloop()