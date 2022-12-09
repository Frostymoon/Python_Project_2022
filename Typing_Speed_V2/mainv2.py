from tkinter import *

root = Tk()

myLabel1 = Label(root, text="GOOD MORNING VIETNAM")
myLabel2 = Label(root, text="LOV THE SMELL OF NAPALM IN THE MORNING")

myLabel1.grid(row=1, column=1)
myLabel2.grid(row=0, column=0)

root.mainloop()