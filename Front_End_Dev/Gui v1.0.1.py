from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter as tk
import turtle
import keyboard


def opentTurtle():
    turtleWindow = tk.Toplevel(root)
    turtleWindow.geometry('700x500')
    canvas = tk.Canvas(master = turtleWindow, width = 500, height = 500)
    canvas.place(x = 0, y = 0)
    t = turtle.RawTurtle(canvas)

    def up():
        t.setheading(90)
        t.forward(10)
        open("user_defined_path.csv", "a").write("f,100,")
    def down():
        t.setheading(270)
        t.forward(10)
        open("user_defined_path.csv", "a").write("b,100,")
    def left():
        t.setheading(180)
        t.forward(10)
        open("user_defined_path.csv", "a").write("l,100,")
    def right():
        t.setheading(0)
        t.forward(10)
        open("user_defined_path.csv", "a").write("r,100,")
    
    tk.Button(master = turtleWindow, text = 'Up', width = 5, command = up).place(x = 570, y = 170)
    tk.Button(master = turtleWindow, text = 'Down', width = 5, command = down).place(x = 570, y = 230)
    tk.Button(master = turtleWindow, text = 'Left', width = 5, command = left).place(x = 550, y = 200)
    tk.Button(master = turtleWindow, text = 'Right', width = 5, command = right).place(x = 600, y = 200)

    tk.Button(master = turtleWindow, text = "Save and Exit", command  = turtleWindow.destroy).place(x = 560, y = 400)    
    
root = tk.Tk()
root.geometry('1000x700')
root.title('Pick n Drop')
root.attributes()

#DPad
tk.Button(root, text = 'Up', height=4, width=10).place(x = 800, y = 400)
tk.Button(root, text = 'Down', height=4, width=10).place(x = 800, y = 500)
tk.Button(root, text = 'Left', height=4, width=10).place(x = 700, y = 450)
tk.Button(root, text = 'Right', height=4, width=10).place(x = 900, y = 450)

#Forklift Functions
tk.Button(root, text = 'Lift', height = 4, width = 20).place(x = 100, y = 400)
tk.Button(root, text = 'Drop', height = 4, width = 20).place(x = 100, y = 500)

#Video Streamer
videoFrame = tk.Frame(root, bg = 'black', height = 150, width = 250).place(x = 50, y = 50)
play = tk.PhotoImage(file = 'Play.png')
play = play.subsample(20,20)
tk.Button(videoFrame, image = play, borderwidth = 0, bg = 'black').place(x = 140, y = 90)

#Demo button
tk.Button(root, text = 'Run Demo', height = 2, width = 20, font = 'bold').place(x = 700, y = 100)

#Turtle
tk.Button(root, text = 'Draw Path', height = 3, width = 5, command = opentTurtle).place(x = 350, y = 100)


#Run Demo
root.mainloop()