from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

root=Tk()


def getname():
    print(entry.get())
    
def yes():
    messagebox.askyesnocancel("edit","do you really")

label=Label(root,text="Enter:-")
label.grid(row=0,column=0)

label=Label(root,text="Registration_number:-")
label.grid(row=1,column=0)

frame=Frame(root,width=100,height=100)
entry=Entry(root,bd=5)
entry.grid(row=0,column=1)
entry=Entry(root,bd=5)
entry.grid(row=1,column=1)
"""

button=Button(root,text="click me",command=getname)
button.grid(row=6,column=1)
"""
check=Radiobutton(root,text="FIRST YEAR",value=1)
check.grid(row=4,column=0)

check=Radiobutton(root,text="SECOND YEAR",value=2)
check.grid(column=1,row=4)

check=Radiobutton(root,text="THIRD YEAR",value=3)
check.grid(column=2,row=4)

check=Radiobutton(root,text="FOURTH YEAR",value=4)
check.grid(column=3,row=4)

check1=Checkbutton(root,text="BIOLOGY")
check2=Checkbutton(root,text="MATHEMATICS")
check3=Checkbutton(root,text="PHYSICS")
check4=Checkbutton(root,text="CHEMISTRY")
check5=Checkbutton(root,text="SOCIAL SCIENCE")
check6=Checkbutton(root,text="ENGLISH")
check7=Checkbutton(root,text="SOFTWARE ENGINEERING")
check8=Checkbutton(root,text="HARDWARE")
check9=Checkbutton(root,text="OTHER")
check1.grid(column=1,row=7,sticky=W)
check2.grid(column=1,row=8,sticky=W)
check3.grid(column=1,row=9,sticky=W)
check4.grid(column=1,row=10,sticky=W)
check5.grid(column=0,row=7,sticky=W)
check6.grid(column=0,row=8,sticky=W)
check7.grid(column=0,row=9,sticky=W)
check8.grid(column=0,row=10,sticky=W)
check9.grid(column=0,row=11,sticky=W)
"""def clicked():
 
    messagebox.askyesnocancel('Message title', 'Message content')
 
btn = Button(label,text='Click here', command=clicked)
btn.grid(row=13,column=2)"""

main=Menu(root)
root.config(menu=main)

filemenu=Menu(main)
main.add_cascade(label="file",menu=filemenu)

save_menu=Menu(filemenu)
filemenu.add_cascade(label="save As",menu=save_menu)

open1=Menu(save_menu)
save_menu.add_cascade(label="document",menu=open1)


edit_menu=Menu(main)
main.add_cascade(label="edit",menu=edit_menu)


bt=Button(root,text="SUBMIT",bg="yellow",command=yes)
bt.grid(column=2,row=12,sticky=W)

bt1=Button(root,text="DUE DATE",bg="red")
bt1.grid(column=3,row=1,sticky=W)

bt2=Button(root,text="EXTEND DATE",bg="blue")
bt2.grid(column=4,row=1,sticky=W)

lab=Label(root,text="TO:-")
lab.grid(row=3,column=4,sticky=W)
en=Entry(root)
en.grid(row=3,column=4,sticky=W)

lab1=Label(root,text="FROM:-")
lab1.grid(row=3,column=4,sticky=W)


root.mainloop()
