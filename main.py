import turtle as t

def createRectangle(sizeX, sizeY, position, fillColor): # Creates rectangular shapes necessary for the creation of the flag
    t.penup()
    t.setpos(position)
    t.fillcolor(fillColor)
    t.pencolor(fillColor)
    t.begin_fill()
    t.pendown()

    for i in range(1, 3): # Repeats repeatable processes
        t.forward(sizeY)
        t.right(90)
        t.forward(sizeX)
        t.right(90)

    t.left(90)

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

t.exitonclick()