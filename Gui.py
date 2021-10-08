from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.geometry('1000x700')
root.title('Pick n Drop')
root.colormapwindows('Black')

#DPad
Button(root, text = 'Up', height=4, width=10).place(x = 800, y = 400)
Button(root, text = 'Down', height=4, width=10).place(x = 800, y = 500)
Button(root, text = 'Left', height=4, width=10).place(x = 700, y = 450)
Button(root, text = 'Right', height=4, width=10).place(x = 900, y = 450)

#Forklift Functions
Button(root, text = 'Lift', height = 4, width = 20).place(x = 100, y = 400)
Button(root, text = 'Drop', height = 4, width = 20).place(x = 100, y = 500)

#Video Streamer
videoFrame = Frame(root, bg = 'black', height = 300, width = 500).place(x = 50, y = 50)
play = PhotoImage(file = 'Play.png')
play = play.subsample(10,10)
tk.Button(videoFrame, image = play, borderwidth = 0, bg = 'black').place(x = 225, y = 120)

#Demo button
Button(root, text = 'Run Demo', height = 2, width = 20, font = 'bold').place(x = 700, y = 100)

#Run Demo
root.mainloop()