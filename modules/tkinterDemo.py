# The tkinter package (“Tk interface”) is the
# standard Python interface to the Tk GUI
# toolkit. Both Tk and tkinter are available
# on most Unix platforms, as well as on Windows
# systems. (Tk itself is not part
# of Python; it is maintained at ActiveState.)

#
# Tkinter is the standard GUI library for Python.
# Python when combined with Tkinter provides
# a fast and easy way to create GUI applications.
# Tkinter provides a powerful object-oriented
# interface to the Tk GUI toolkit.
# Creating a GUI application using Tkinter
# is an easy task.


try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)
# tkinter._test()

mainWindow=tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x640+8+400")


label= tkinter.Label(mainWindow,text="Hello World")
label.pack(side='top')

canvas=tkinter.Canvas(mainWindow,relief='raised',borderwidth=1)
canvas.pack(side='left')

button1=tkinter.Button(mainWindow,text="Button1")
button2=tkinter.Button(mainWindow,text="Button2")

button1.pack(side="left",anchor="n")
button2.pack(side="left",anchor="s")
# e
mainWindow.mainloop()





