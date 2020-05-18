import turtle, random
draw = turtle.Turtle()
draw.color("Blue")
draw.shape("turtle")
draw.penup()
turnCount = 0
eg1 = "false"
eg2 = "false"
eg3 = "false"
eg4 = "false"
def eggSetup(type):
    type.shape("circle")
    type.penup()
    eggX = random.randint(-300, 300)
    eggY = random.randint(-300,300)
    type.goto(eggX,eggY)

egg1 = turtle.Turtle()
eggSetup(egg1)

egg2 = turtle.Turtle()
eggSetup(egg2)

egg3 = turtle.Turtle()
eggSetup(egg3)

egg4 = turtle.Turtle()
eggSetup(egg4)

def moveRight(type):
    type.setheading(0)
    if (type == draw):
        type.forward(40)
    else:
        type.forward(10)
def moveUp(type):
    type.setheading(90)
    if (type == draw):
        type.forward(40)
    else:
        type.forward(10)

def moveLeft(type):
    type.setheading(180)
    if (type == draw):
        type.forward(40)
    else:
        type.forward(10)
    
def moveDown(type):
    type.setheading(270)
    if (type == draw):
        type.forward(40)
    else:
        type.forward(10)

print ("Help the Turtle collect all of the eggs as quick as possible.")
while True:
    direction= raw_input("Pick a direction: (left/up/right/down): ")
    collision1 = draw.distance(egg1)
    collision2 = draw.distance(egg2)
    collision3 = draw.distance(egg3)
    collision4 = draw.distance(egg4)             
    if direction == ("right"):
        moveRight(draw)
    elif direction == ("left"):
        moveLeft(draw)
    elif direction == ("up"):
        moveUp(draw)
    elif direction == ("down"):
        moveDown(draw)
    else:
        print("Please enter a valid choice with first letters being lowercase")
    if (collision1 < 30) :
        egg1.color("white")
        eg1 = ("true")
    if(collision2 < 30):
        egg2.color("white")
        eg2 = ("true")
    if(collision3 < 30):
        egg3.color("white")
        eg3 = ("true")
    if(collision4 < 30):
        egg4.color("white")
        eg4 = ("true")
    turnCount += 1
    if(eg1 == "true" and eg2 == "true" and eg3 == "true" and eg4 == "true"):
        print ("You Won in ", turnCount, " turns.")
        quit()
 
