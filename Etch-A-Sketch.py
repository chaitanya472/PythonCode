import turtle
draw = turtle.Turtle()
draw.color("black")

def Color():
    value =("false")
    while value != ("true"):
            color = raw_input("Please pick a color:(red/orange/yellow/green/blue/violet/blackcolo):")
            if color == ("red"):
                draw.color("Red")
                value = ("true")
            elif color == ("orange"):
                draw.color("Orange")
                value = ("true")
            elif color == ("yellow"):
                draw.color("Yellow")
                value = ("true")
            elif color == ("green"):
                draw.color("Green")
                value = ("true")
            elif color == ("blue"):
                draw.color("Blue")
                value = ("true")
                value = ("true")
            elif color == ("violet"):
                draw.color("Violet")
                value = ("true")
            elif color == ("black"):
                draw.color("Black")
                value = ("true")
            else:
                print("Please enter a valid choice with first letters being lowercase")
def moveRight():
    draw.setheading(0)
    draw.forward(20)

def moveUp():
    draw.setheading(90)
    draw.forward(20)

def moveLeft():
    draw.setheading(180)
    draw.forward(20)

def moveDown():
    draw.setheading(270)
    draw.forward(20)

while True:
    direction= raw_input("Pick a direction: (left/up/right/down) or say color to change your color: ")
    if direction == ("right"):
        moveRight()
    elif direction == ("left"):
        moveLeft()
    elif direction == ("up"):
        moveUp()
    elif direction == ("down"):
        moveDown()
    elif direction == ("color"):
        Color()
    else:
        print("Please enter a valid choice with first letters being lowercase")
