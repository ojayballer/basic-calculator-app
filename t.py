from tkinter import *
root=Tk()
e=Entry(root,width=50)
e.pack()
def getEntry():
    v=Label(root,text="Hello"+"<"+e.get()+">").pack()
myButton=Button(root,text="Greet",command=getEntry,fg="blue"
                ,bg="yellow",padx=2.5,pady=2.5).pack()
root.mainloop()
