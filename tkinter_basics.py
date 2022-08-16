from tkinter import Label
from tkinter import Checkbutton
from tkinter import Button
from tkinter.tix import Tk
from turtle import pos, position
win = Tk(screenName=None,baseName=None,className= "Hello World")
win.geometry()
b= Button(win,text="Print",bg="blue")
b.pack()
c=Label(win,text="Hello!! How are you all working there , hoping the health for everyone out there",bg="pink")
c.pack()
d=Checkbutton(win,text="help me")
d.pack()
# win indicates the name of the main window object
# Tk method is used to create the main window
win.mainloop()
# above is used to run the application and it's actually an infinite loop 