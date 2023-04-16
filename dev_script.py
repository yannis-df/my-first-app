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

    for widget in frame.winfo_children():
        widget.destroy()

    filename = tk.filedialog.askopenfilename(initialdir="/", title="Select File",
                                             filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.06)

openFile = tk.Button(root, text="Open file", padx=10, pady=5, fg="white", 
                     bg="steelblue", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", 
                    bg="steelblue", command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')