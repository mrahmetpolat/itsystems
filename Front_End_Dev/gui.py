
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
#turtle import
import turtle
import random
from turtle import*

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("PicknDrop")
window.iconbitmap('image_1.png')


window.geometry("1440x1086")
window.configure(bg = "#2B3648")


canvas = Canvas(
    window,
    bg = "#2B3648",
    height = 1086,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    292.0000000000001,
    75.0,
    anchor="nw",
    text="Live Video Feed ",
    fill="#AFBDD1",
    font=("Roboto Medium", 20 * -1)
)

canvas.create_rectangle(
    292.0000000000001,
    109.0,
    984.0000000000001,
    635.0,
    fill="#EBEBEB",
    outline="")

canvas.create_rectangle(
    1026.0,
    107.0,
    1378.0,
    385.0,
    fill="#212936",
    outline="")

canvas.create_rectangle(
    1025.0,
    653.0,
    1377.0,
    932.0,
    fill="#212936",
    outline="")

canvas.create_rectangle(
    1023.0000000000001,
    404.0,
    1378.0,
    635.0,
    fill="#212936",
    outline="")

button_left_arrow = PhotoImage(
    file=relative_to_assets("leftarrow.png"))
left_arrow = Button(
    image=button_left_arrow,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Left arrow clicked"),
    relief="flat"
)
left_arrow.place(
    x=1114.0,
    y=503.0,
    width=77.0,
    height=46.0
)

button_right_arrow = PhotoImage(
    file=relative_to_assets("rightarrow.png"))
right_arrow = Button(
    image=button_right_arrow,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Right arrow clicked"),
    relief="flat"
)
right_arrow.place(
    x=1236.0,
    y=503.0,
    width=76.0,
    height=46.0
)

button_drop = PhotoImage(
    file=relative_to_assets("drop.png"))
drop= Button(
    image=button_drop,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Drop clicked"),
    relief="flat"
)
drop.place(
    x=1078.249267578125,
    y=700.5538330078125,
    width=246.461669921875,
    height=52.8419189453125
)

button_lift = PhotoImage(
    file=relative_to_assets("lift.png"))
lift= Button(
    image=button_lift,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Lift clicked"),
    relief="flat"
)
lift.place(
    x=1078.249267578125,
    y=787.0223999023438,
    width=246.461669921875,
    height=52.8419189453125
)
def open_turtle():
    turle_child = Tk.Toplevel(window)
    turle_child.geometry("800x800")
    turle_child.title('Turtle')
    def up():
        tl.setheading(90)
        tl.forward(10)
    def down():
        tl.setheading(270)
        tl.forward(10)
    def left():
        tl.setheading(180)
        tl.forward(10)
    def right():
        tl.setheading(0)
        tl.forward(10)




    turtle.listen()
    turtle.onkey(up,'Up')
    turtle.onkey(down,'Down')
    turtle.onkey(left,'Left')
    turtle.onkey(right,'Right')

button_draw = PhotoImage(
    file=relative_to_assets("draw.png"))
draw = Button(
    image=button_draw,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_turtle(),
    relief="flat"
)

draw.place(
    x=1079.200927734375,
    y=284.4461975097656,
    width=246.461669921875,
    height=52.8419189453125
)

button_up_arrow = PhotoImage(
    file=relative_to_assets("uparrow.png"))
up_arrow = Button(
    image=button_up_arrow,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Up arrow clicked"),
    relief="flat"
)
up_arrow.place(
    x=1191.0,
    y=421.0,
    width=45.0,
    height=77.0
)

button_down_arrow = PhotoImage(
    file=relative_to_assets("downarrow.png"))
down_arrow = Button(
    image=button_down_arrow,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Down button clicked"),
    relief="flat"
)
down_arrow.place(
    x=1191.0,
    y=552.0,
    width=45.0,
    height=77.0
)

button_demo = PhotoImage(
    file=relative_to_assets("demo.png"))
demo = Button(
    image=button_demo,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Demo clicked"),
    relief="flat"
)
demo.place(
    x=1079.200927734375,
    y=181.64462280273438,
    width=246.461669921875,
    height=52.8419189453125
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    176.0000000000001,
    194.0,
    image=image_image_1
)
window.resizable()
window.mainloop()
