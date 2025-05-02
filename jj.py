from tkinter import*
from PIL import ImageTk,Image #for adding images
root=Tk()
image_number=0

root.title("image viewer")
#root.iconbitmap('')
myImage1=ImageTk.PhotoImage(Image.open("pictures/image11.jpg"))
myImage2=ImageTk.PhotoImage(Image.open("pictures/image2.jpg"))
myImage3=ImageTk.PhotoImage(Image.open("pictures/image3.jpg"))#we store image in a variable
my_label=Label(image=myImage1)
imageList=[myImage1,myImage2,myImage3]
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global forward_button
    global backward_button

    my_label.grid_forget()
    my_label=Label(image=[imageList-1])
    my_label.grid(row=0,column=0,columnspan=3)
    foward_button=Button(root,text=">>>",command=lambda:forward(2))
def backward():
    global my_label
    global forward_button
    global backward_button


backward_button=Button(root,text="<<<",command=lambda:backward)
Exit_button=Button(root,text="exit button",command=root.quit)
foward_button=Button(root,text=">>>",command=lambda:forward(image_number+1))
backward_button.grid(row=1,column=0)
Exit_button.grid(row=1,column=1)
foward_button.grid(row=1,column=3)




root.mainloop()