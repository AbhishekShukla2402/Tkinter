from tkinter import *

def fetch(entry1,entry2,entry3):
    print("Name : '%s'" % entry1.get())
    print("Job  : '%s'" % entry2.get())
    print("Pay  : '%s'" % entry3.get())
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    
root=Tk()
root.resizable(False, False)
row = Frame(root)
lab = Label(row, width=5, text="Name")
ent=Entry(row)
row.pack(side=TOP, fill=X)
lab.pack(side=LEFT)
ent.pack(side=RIGHT, expand=YES, fill=X)


row2 = Frame(root)
lab2 = Label(row2,width=5, text="Job")
ent2=Entry(row2)
row2.pack(side=TOP, fill=X)
lab2.pack(side=LEFT)
ent2.pack(side=RIGHT, expand=YES, fill=X)


row3 = Frame(root)
lab3 = Label(row3,width=5, text="Pay")
ent3=Entry(row3)
row3.pack(side=TOP, fill=X)
lab3.pack(side=LEFT)
ent3.pack(side=RIGHT, expand=YES, fill=X)

Button(root, text='Fetch', command= (lambda: fetch(ent,ent2,ent3))).pack()
root.mainloop()
