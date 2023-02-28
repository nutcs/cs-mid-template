from tkinter import *

window = Tk()

window.title("HV-Week2_ณัฐพล_สลางสิงห์_1650704388")
window.geometry("600x450")
window.configure(bg="#ebc79d")
window.option_add('*font','Garamond 18 bold')
window.grid_columnconfigure((1,2),weight=1)

bgs="#ebc79d"
fgs="#0000ff"
bgText="#dfade8"
bgBox = "#c0c0c0"
wBox=13
pdA = 8
main = 1
c1 = 1
c2 = 2
stickys = E
st =W

def create(st):
    header = Label(window,text="Find average of 3 numbers Program",bg=bgs,fg=fgs)
    header.grid(row=0,column=main,pady=20,columnspan=2,sticky=st,padx=40)

    number1 = Label(window,text="Number1 :",fg=fgs,bg="#b0e3e9")
    number1.grid(row=1,column=c1,pady=pdA,sticky=stickys,padx=40)
    box1 = Entry(window,width=wBox,bg=bgBox,borderwidth=4, relief="solid")
    box1.grid(row=1,column=c2,pady=pdA,sticky=st,padx=80,ipady=3)
    
    number2 = Label(window,text="Number2 :",fg=fgs,bg=bgText)
    number2.grid(row=2,column=c1,pady=pdA,sticky=stickys,padx=40)
    box2 = Entry(window,width=wBox,bg=bgBox,borderwidth=4, relief="solid")
    box2.grid(row=2,column=c2,pady=pdA,sticky=st,padx=80,ipady=3)
    
    number3 = Label(window,text="Number3 :",fg=fgs,bg=bgText)
    number3.grid(row=3,column=c1,pady=pdA,sticky=stickys,padx=40)
    box3 = Entry(window,width=wBox,bg=bgBox,borderwidth=4, relief="solid")
    box3.grid(row=3,column=c2,pady=pdA,sticky=st,padx=80,ipady=3)

    button1 = Button(window,text="Register",width=13,bg="#efefef",borderwidth=4, relief="solid")
    button1.grid(row=4,column=c1,pady=15,ipady=8,sticky=stickys)
    button2 = Button(window,text="Find Average",width=13,bg="#efefef",borderwidth=4, relief="solid")
    button2.grid(row=4,column=c2,pady=15,ipady=8,padx=15)

    cName = 'Created by nutthapon salangsing, ID : 1650704388'
    footer = Label(window,text=cName,bg=bgs,fg=fgs)
    footer.grid(row=5,column=main,pady=5,columnspan=2,sticky=st)
create(st)
window.mainloop()


