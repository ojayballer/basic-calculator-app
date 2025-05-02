from tkinter import *

root=Tk()
#creating label widget
myLabel1=Label(root,text="Hello world!")
myLabel2=Label(root,text="my name is omojire!")

#Shoving it onto the screen
myLabel1.grid(row=0,column=1)
myLabel2.grid(row=1,column=1)
#event loop
root.mainloop()

