import turtle as t


# Flag - Taha Ghumman

# Rectangle Function
def createRectangle(sizeX, sizeY, position, fillColor, penColor = None):
    t.penup()
    t.setpos(position)
    t.fillcolor(fillColor)
    t.pencolor(penColor or fillColor)
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

def onKey(x, y):
    print("Reached")
#Flag Size
flagSizeX = 350
flagSizeY = 550

#Flag Colors
redColor = (238,42,53)
blackColor = (0, 0, 0)
greenColor = (0,151,54)
whiteColor = (255,255,255)

t.speed(0)
t.colormode(255)

# Flag Base
createRectangle(flagSizeX, flagSizeY, (-300, 200), greenColor)
t.back(flagSizeX/3)

createRectangle(flagSizeY, flagSizeX/3, t.pos(), blackColor)
t.right(90)
t.back(flagSizeX/3)

createRectangle(flagSizeY, flagSizeX/3, t.pos(), whiteColor)

# Flag Triangle
t.penup()
t.setpos(-300, 200)
t.pendown()
t.begin_fill()
t.color(redColor)
t.left(-225)
t.forward(flagSizeY/2.22)
t.left(-90)
t.forward(flagSizeY/2.22)
t.end_fill()



# Fist - Troy Williams

# Wrist
t.setheading(82)
createRectangle(35, 80, (-40,-70), greenColor, whiteColor)
t.setheading(85)
createRectangle(30, 90, (1,-77), blackColor, whiteColor)

# Palm
t.setheading(68)
createRectangle(25, 75, (12,-15), blackColor)
t.setheading(140)
createRectangle(35, 45, (14,1), blackColor)
t.setheading(140)
createRectangle(35, 80, (-15,-25), greenColor)

# Fingers
t.setheading(58)
createRectangle(25, 30, (-25,105), redColor, whiteColor)
t.setheading(55)
createRectangle(25, 35, (-3,90), redColor, whiteColor)
t.setheading(50)
createRectangle(25, 60, (3,58), redColor, whiteColor)
t.setheading(48)
createRectangle(25, 60, (24,42), redColor, whiteColor)

# Thumb
t.setheading(58)
createRectangle(40, 90, (-76,26), greenColor)
t.setheading(148)
createRectangle(30, 65, (11,43), greenColor, whiteColor)

# Writing
t.penup()
t.pencolor(whiteColor)

# Top Text
t.goto(-90,130)
t.pendown()
t.write("F R E E", font=("Futura", 40, "bold"))
t.penup()

# Bottom Text
t.goto(-140,-150)
t.pendown()
t.write("PALESTINE", font=("Futura", 40, "bold"))
t.penup()

t.onclick(onKey, 2)
t.exitonclick()
