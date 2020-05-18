import turtle
draw = turtle.Turtle()
draw.speed(500)
draw.pencolor("White")
draw.goto(0, 100)


def triangle():
    draw.begin_fill()
    for time in range (1,3):
        draw.left(60)
        draw.forward(40)
    draw.right(120)
    draw.end_fill()
    
    
        
def shapes(type):
    draw.fillcolor(type)
    draw.begin_fill()
    for loop in range (1,5):
        draw.forward(120)
        draw.right(90)
    draw.end_fill()
    draw.right(10)
    draw.forward(120)
    draw.begin_fill()
    draw.circle(75)
    draw.backward(100)
    
    
for lap in range (1,10):        
    shapes("Blue")
    shapes("Red")
    shapes("Yellow")
    shapes("Green")
    shapes("Black")
    shapes("Purple")
    shapes("Pink")
    shapes("Orange")
    shapes("Brown")

