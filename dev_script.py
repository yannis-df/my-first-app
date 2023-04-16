# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:26:38 2023

@author: yannis
"""
import os
import tkinter as tk
from tkinter import filedialog, Text
# from tkinter import filedialog

root = tk.Tk()

apps = []
def addApp():
    filename = tk.filedialog.askopenfilename(initialdir="/", title="Select File",
                                             filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

# frameL = tk.Frame(root, bg="white")
# frameL.place(relwidth=0.1, relheight=0.1, relx=0.1, rely=0.1)

# frameR = tk.Frame(root, bg="white")
# frameR.place(relwidth=0.1, relheight=0.1, relx=0.8, rely=0.1)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.06)

# my_button = tk.Button(frameL, text="my_button", padx=10, pady=5, fg="white", bg="firebrick")
# my_button.pack()

openFile = tk.Button(root, text="Open file", padx=10, pady=5, fg="white", 
                     bg="steelblue", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="steelblue")
runApps.pack()

root.mainloop()
