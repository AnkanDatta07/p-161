# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:07:37 2023

@author: Ankan Datta
"""

from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image

root = Tk()
root.title("HTML IDE")
root.minsize(650, 650)
root.maxsize(650, 650)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
save_image = ImageTk.PhotoImage(Image.open("save.png"))
live = ImageTk.PhotoImage(Image.open("arrow_left.png"))

file_label = Label(root, text = "FILE NAME")
file_label.place(relx = 0.5, rely = 0.02, anchor=CENTER)

file_input = Entry(root)
file_input.place(relx = 0.7, rely = 0.02, anchor=CENTER)

note_text = Text(root, height = 35, width = 80, bg = "grey")
note_text.place(relx = 0.5, rely = 0.5, anchor=CENTER)


name = ""

def openFile(): 
    global name
    note_text.delete(1.0, END)
    file_input.delete(0, END)
    text_file = filedialog.askopenfilename(title = "Open text file", filetypes = (("Text file", "*.html"), ))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    file_input.insert(END, formated_name)
    root.title(formated_name)
    text_file = open(name, 'r')
    paragraph = text_file.read
    note_text.insert(END, paragraph)
    text_file.close
    
button1 = Button(root, text = "Open File", image = open_image, command = openFile)
button1.place(relx = 0.03, rely = 0.01)

button2 = Button(root, text = "Save File", image = save_image)
button2.place(relx = 0.09, rely = 0.01)

button3 = Button(root, text = "Start Live", image = live)
button3.place(relx = 0.15, rely = 0.01)

root.mainloop()