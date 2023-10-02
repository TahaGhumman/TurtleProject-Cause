import turtle as t

def createRectangle(sizeX, sizeY, position, fillColor, penColor = None):
    t.penup()
    t.setpos(position)
    t.fillcolor(fillColor)
    t.pencolor(penColor or fillColor)
    t.begin_fill()
    t.pendown()
    t.degrees(360)
    t.forward(sizeY)
    t.right(90)
    t.forward(sizeX)
    t.right(90)
    t.forward(sizeY)
    t.right(90)
    t.forward(sizeX)
    t.end_fill()
    return

flagSizeX = 350
flagSizeY = 550

createRectangle(flagSizeX, flagSizeY, (-300, 200), "green")
t.back(flagSizeX/3)
createRectangle(flagSizeY, flagSizeX/3, t.pos(), "black")
t.right(90)
t.back(flagSizeX/3)
createRectangle(flagSizeY, flagSizeX/3, t.pos(), "white")

#fist - troy williams
#~~~~

#wrist
t.setheading(82)
createRectangle(35, 80, (-40,-70), "green", "white")
t.setheading(85)
createRectangle(30, 90, (1,-77), "black", "white")

#palm
t.setheading(68)
createRectangle(25, 75, (12,-15), "black")
t.setheading(140)
createRectangle(35, 45, (14,1), "black")
t.setheading(140)
createRectangle(35, 80, (-15,-25), "green")

#fingers
t.setheading(58)
createRectangle(25, 30, (-25,105), "red", "white")
t.setheading(55)
createRectangle(25, 35, (-3,90), "red", "white")
t.setheading(50)
createRectangle(25, 60, (3,58), "red", "white")
t.setheading(48)
createRectangle(25, 60, (24,42), "red", "white")

#thumb
t.setheading(58)
createRectangle(40, 90, (-76,26), "green")
t.setheading(148)
createRectangle(30, 65, (11,43), "green", "white")

#writing - troy williams
#~~~~~~~
t.penup()
t.pencolor("white")

#top
t.goto(-90,130)
t.pendown()
t.write("F R E E", font=("Futura", 40, "bold"))
t.penup()

#bottom
t.goto(-140,-150)
t.pendown()
t.write("PALESTINE", font=("Futura", 40, "bold"))
t.penup()

#t.done()
t.exitonclick()


print("Reached")
