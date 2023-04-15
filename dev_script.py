# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:26:38 2023

@author: yanni
"""
## path to env: C:\Users\yanni\Documents\Code\Python\dev_project\env\Scripts\activate.bat
#%%
import os
import tkinter as tk
from tkinter import filedialog, Text

#%%

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frameL = tk.Frame(root, bg="white")
frameL.place(relwidth=0.1, relheight=0.1, relx=0.1, rely=0.1)

frameR = tk.Frame(root, bg="white")
frameR.place(relwidth=0.1, relheight=0.1, relx=0.8, rely=0.1)

frameC = tk.Frame(root, bg="white")
frameC.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.6)

my_button = tk.Button(frameL, text="my_button", padx=10, pady=5, fg="white", bg="firebrick")
my_button.pack()

root.mainloop()