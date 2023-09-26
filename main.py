import turtle as t

def createRectangle(sizeX, sizeY, position, fillColor):
    t.penup()
    t.setpos(position)
    t.fillcolor(fillColor)
    t.pencolor(fillColor)
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

createRectangle(flagSizeX, flagSizeY, (-300, 200), "red")
print(t.position())
t.back(flagSizeY/3)
createRectangle(flagSizeX, flagSizeY/3, t.position(), "black")

t.done()