from tkinter import*
root=Tk()
root.title("i am coding :)  xoxo")
e=Entry(root,width=50,fg="blue",bg="white")
e.pack()
fr=LabelFrame(root,text=" ",padx=50,pady=50).pack()
frame=LabelFrame(root,text="ts is my frame",padx=5,pady=5)
frame.pack(padx=10,pady=10)
#b=Button(frame,text="clickkkkkkk!")
#b.pack()
def mylab():
    myLabel=Label(root,text=r.get())
    myLabel.pack()

r=StringVar()
r1=IntVar()
Radiobutton(fr,text="option 1",variable=r,value="omojire",command=mylab).pack()
Radiobutton(frame,text="option 2",variable=r,value="murewa",command=mylab).pack()

root.mainloop()