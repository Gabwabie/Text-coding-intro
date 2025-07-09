import pygame
from tkinter import *
from tkinter import messagebox

#Setup Tkinter window
root = Tk()
root.geometry("200x200")

#Function for displaying warning message
#this will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

def msg2():
    messagebox.showinfo("About Me", "My name is Gabriellle. I am 15 and I like coding.")

#Adding button widget to window
button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

button2 = Button(root, text="About me", command=msg2)
button2.place(x=40, y=160)

#Entering main event loop
root.mainloop()