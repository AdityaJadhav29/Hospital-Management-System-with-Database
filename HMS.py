from tkinter import *
from PIL import Image, ImageTk
#from update import Application
import os

root=Tk()
root.geometry("1920x1080")
root.title("Hospital Management System")

image = Image.open('hospital.png')
photo_image = ImageTk.PhotoImage(image)
label =Label(root, height =1920, width=1080,image = photo_image)
label.pack()

#function to call update
def callbackup():
    filename = 'update.py'
    os.system(filename)
    
#function to call appointment
def callbackupap():
    filename = 'appointment.py'
    os.system(filename)    

b4 =Label(root, font=('arial',50),text = "General Hospital").place(x = 500,y = 50)

    #button to call Appoinments
b=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="Appoinments",command=callbackupap)
b.place(x=100,y=650)

    #button to call update
b1=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="Update",command=callbackup)
b1.place(x=425,y=650)

#b2=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="Display")
#b2.place(x=650,y=650)



root.mainloop()
    



