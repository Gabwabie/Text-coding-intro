import pygame
from tkinter import *

#root window
root = Tk()
root.geometry("200x300")
root.title("main")
l = Label(root, text= "This is root window")

#top window
top = Toplevel()
top.geometry("180x100")
top.title("toplevel")
l2 = Label(top, text= "This is toplevel window")

root.mainloop()