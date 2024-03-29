import turtle as t
from time import sleep
from typing import *

"""
Creating the Palestinian Flag for the crisis in Palestine/Israel using Python Turtle. 

Focuses on exerting skills within if statements, for loops, variables, and understanding Python Turtle. 
"""

t.speed(0)
t.colormode(255)
t.hideturtle()

#Window
window = t.Screen()
window.title('Free Palestine')

#Flag Size
flagSizeX = 350
flagSizeY = 550

#Flag Colors
redColor = (238,42,53)
blackColor = (0, 0, 0)
greenColor = (0,151,54)
whiteColor = (255,255,255)

# Flag - Taha Ghumman

# Creates Flame Wisp - Rashed Amani
def createWisp(radius):
    """
    Creates a triangular 'wisp' shape.

    :params radius: the length from the centre of the circle, creates the width of the wisp.

    """
    t.circle(radius, 90)
    t.left(180)
    t.circle(radius, 90)

# Rectangle Function - Taha Ghumman
def createRectangle(sizeX: int, sizeY: int, position: tuple, fillColor: Any, penColor:Any = None):
    """
    Creates a rectangle object based on your given 'x' and 'y' sizes and positions it as 'position'. 
    It uses 'fillColor' as the color to use within of the rectangle and 'penColor' for the outline.
    'penColor' is not a needed argument as it defaults to "None" and thus uses the fillColor.

    :params sizeX: The x size of the rectangle
            sizeY: The y size of the rectangle
            position: The (x, y) coordinate within the Python Window
            fillColor: The color used to fill the rectangle
            penColor: The penColor used to outline the rectangle
    """

    t.penup()
    t.setpos(position)
    t.fillcolor(fillColor)
    t.pencolor(penColor or fillColor)
    t.begin_fill()
    t.pendown()

    for i in range(1, 3): # Repeats creating the borders of the rectangle
        t.forward(sizeY)
        t.right(90)
        t.forward(sizeX)
        t.right(90)

    t.left(90)

    t.end_fill()
    return

# Flag - Taha Ghumman
def createFlag(flagSizeX: int, flagSizeY: int):
    """
    Creates the Palestinian flag, by first making the base of the flag green, 
    then adding a black rectangle from the top of the flag towards 1/3rd inwards,
    then creates a white rectangle underneath the black rectangle 1/3rd from the bottom.


    :params flagSizeX: Represents how far the flag stretches horizontally
            flagsizeY: Represents how far the flag stretches vertically
    """
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

# Fist of Power - Troy Williams
def createFist():
    """
    Creates the 'Fist of Power' by using the rectangle function allowing it to first form the wrist portion,
    then the palm portion, then the fingers and finally the thumb.

    """
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

# Create Text - Troy Williams
def writingText():
    """
    Creates the top text writing, "F R E E" in the black section of the flag,
    and a bottom text writing, "PALESTINE" in the green section of the flag.
    """
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

# Creates Blinking Flames - Rashed Amani
def createFlame():
    """
    Creates multi colored flames using the wisp function to create each 'wisp' of flame.
    The flame colors transition from orange, red, and yellow and repeats 50 times, creating a blinking effect.
    """
    
    t.color('red', 'orange')

    t.pensize(1)
    t.width()
    t.pencolor('red')
    t.fillcolor('orange')

    t.penup()
    t.setposition(-300, 200)
    t.speed(0)
    t.begin_fill()

    t.pendown()

    # Create Blinking Effect
    for i in range(50):
        t.begin_fill()
        t.setheading(0)
        if i % 3 == 1:
            t.color("orange", "red")
        elif i % 3 == 2:
            t.color("red", "yellow")
        else:
            t.color("yellow", "orange")
        for x in range(5):
            createWisp(55)
        t.left(180)
        t.forward(5 * 55 * 2)
        t.end_fill()
        sleep(0.25)

# Main
createFlag(flagSizeX, flagSizeY)
createFist()

# Writing - Troy Williams
t.penup()
t.pencolor(whiteColor)

writingText()

# Flames - Rashed Omani
createFlame()

# Finish
t.exitonclick()
