from tkinter import *
root=Tk()
root.title("simple calculator app")
e=Entry(root,width=35,borderwidth=5,fg="blue",bg="white") 
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
   first_num = e.get()
   global f_num
   global math
   math="addition"
   f_num = int(first_num)
   e.delete(0, END)
   
def button_equal():
    second_num=e.get()
    e.delete(0,END)
    if math == "addition":
       e.insert(0,f_num + int(second_num))
    if math == "subtraction":
       e.insert(0,f_num - int(second_num))
    if math == "multiplication":
        e.insert(0,f_num * int(second_num))
    if math == "division":
       e.insert(0,f_num / int(second_num))
   
def button_subtract():
   first_num = e.get()
   global f_num
   global math
   math="subtraction"
   f_num = int(first_num)
   e.delete(0, END)
   
    
def button_multiply():
   first_num = e.get()
   global f_num
   global math
   math="multiplication"
   f_num = int(first_num)
   e.delete(0, END)
   
def button_divide():
   first_num = e.get()
   global f_num
   global math
   math="division"
   f_num = int(first_num)
   e.delete(0, END)
   

   
#define buttons
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))

button_add=Button(root,text="+",padx=40,pady=20,command=button_add)
button_equal=Button(root,text="=",padx=91,pady=20,command=button_equal)
button_clear=Button(root,text="Clear",padx=79,pady=20,command=button_clear)

button_subtract=Button(root,text="-",padx=41,pady=20,command=button_subtract)
button_multiply=Button(root,text="X",padx=40,pady=20,command=button_multiply)
button_divide=Button(root,text="/",padx=41,pady=20,command=button_divide)
button=[button_1,button_2,button_3]
buttontwo=[button_4,button_5,button_6] 
buttonthree=[button_7,button_8,button_9]

i=0
for butt in button:
    butt.grid(row=3,column=i)
    i+=1
i=0   
for butt in buttontwo:
    butt.grid(row=2,column=i)
    i+=1
i=0
for butt in buttonthree:
    butt.grid(row=1,column=i)
    i+=1
button_0.grid(row=4,column=0)


button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)



root.mainloop()
