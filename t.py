import turtle
from random import randint as r
from tkinter import *
thingy = turtle.Turtle()
my_window = turtle.Screen()
colors = ["blue","green","red","yellow","purple"]
def get():
    #retrieve values from interface then call the draw subroutine
    numShapes = weight_enter.get()
    minSides = height_enter.get()
    maxSides = sides_enter.get()
    draw(numShapes,minSides,maxSides)
def draw(n,minimum,maximum):
    #generate random color and number of sides
    #and goto the coordinates for the begenning of each shape
    #it then draws the shape and fills with the random color
    for x in range(int(n)):
        thingy.penup()
        thingy.goto(r(-200,200),r(-200,200))
        thingy.right(r(0,360))
        color = r(0,(len(colors)-1))
        thingy.color(colors[color])
        thingy.begin_fill()
        thingy.pendown()
        sides = r(int(minimum),int(maximum))
        for y in range(sides):
            thingy.forward(50)
            thingy.right(360-(360/(sides)))
        thingy.end_fill()

window = Tk()
window.title("Shape Maker")
window.config(bg="#84fc80")
frame = Frame(window)
frame.config(bg="white")
frame.grid(padx=20,pady=20,column=0,row=0)

headers=Label(frame,text = "Sign Up")
headers.config(bg="#84fc80",font=("Arial Bold",26))
headers.grid(column=0,row=0,columnspan=4,padx=10,pady=10,sticky="ew")

header = Label(frame,text="Enter number of shapes")
header.config(bg="#b6bac1", font=("Arial Bold",18))
header.grid(column=0,row=1,columnspan=2,padx=10,pady=10,sticky="ew")

weight_enter = Entry(frame)
weight_enter.config(bg="white",font = ("Arial Bold",18),width=24, justify="center")
weight_enter.grid(column=2,row=1,columnspan=2,padx=10,pady=10)

header = Label(frame,text="Enter minimum number of sides")
header.config(bg="#b6bac1", font=("Arial Bold",18))
header.grid(column=0,row=2,columnspan=2,padx=10,pady=10,sticky="ew")

height_enter = Entry(frame)
height_enter.config(bg="white",font = ("Arial Bold",18),width=24, justify="center")
height_enter.grid(column=2,row=2,columnspan=2,padx=10,pady=10)

header = Label(frame,text="Enter maximum number of sides")
header.config(bg="#b6bac1", font=("Arial Bold",18))
header.grid(column=0,row=3,columnspan=2,padx=10,pady=10,sticky="ew")

sides_enter = Entry(frame)
sides_enter.config(bg="white",font = ("Arial Bold",18),width=24, justify="center")
sides_enter.grid(column=2,row=3,columnspan=2,padx=10,pady=10)


button = Button(frame,command=get,text="Press to make shapes")
button.config(bg="#4fa04d",font=("Arial Bold",18),)
button.grid(column=0,row=4,columnspan=4,padx=20,pady=20)
