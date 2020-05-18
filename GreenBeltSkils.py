import turtle
calvin=turtle.Turtle()
def drawSquare():
    calvin.shape("turtle")
    calvin.fillcolor("purple")
    calvin.pencolor("red")
    calvin.forward(50)
    calvin.right(90)
    calvin.pencolor("green")
    calvin.forward(50)
    calvin.right(90)
    calvin.pencolor("yellow")
    calvin.forward(50)
    calvin.right(90)
    calvin.pencolor("blue")
    calvin.forward(50)



for lap in range(0, 36):
    drawSquare()
    calvin.right(10)
    calvin.circle(20)









