import turtle

t = turtle.Turtle()
t.speed(1)


def up():
    t.setheading(90)
    t.forward(50)
    open("user_defined_path2.csv", "a").write("f.50,")

def down():
    t.setheading(270)
    t.forward(50)
    open("user_defined_path2.csv", "a").write("b.50,")

def left():
    t.setheading(180)
    t.forward(50)
    open("user_defined_path2.csv", "a").write("l.50,")

def right():
    t.setheading(0)
    t.forward(50)
    open("user_defined_path2.csv", "a").write("r.50,")

 
turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()
