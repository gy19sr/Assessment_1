# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:54:40 2019

@author: gy19sr
"""

import Tkinter as Tk


def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var )
scale.pack(anchor=CENTER)

button = Button(root, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()