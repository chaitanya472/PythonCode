import turtle, sys
draw= turtle.Turtle()
draw.right(90)

def retry():
    restart = raw_input("Would you want to play again yes or no: ")
    if (restart == "yes"):
        print("Restarting game")
        draw.reset()
        draw.right(90)
        play(100, 50)
    if (restart == "Yes"):
        print("Restarting game")
        draw.reset()
        draw.right(90)
        play(100, 50)
    elif(restart == "No"):
        print("Ending game")
        sys.exit()
    elif(restart == "no"):
        print("Ending game")
        sys.exit()
        
def turnRight():
    draw.right(30)
    draw.forward(35)
    draw.left(30)
    draw.color ("blue")
    draw.stamp()
    
def turnDown():
    draw.forward(70)
    draw.color ("blue")
    draw.stamp()
    
def turnUp():
    draw.left(180)
    draw.forward(125)
    draw.right(180)
    draw.color ("blue")
    draw.stamp()
    
def turnLeft():
    draw.left(30)
    draw.forward(35)
    draw.right(30)
    draw.color ("blue")
    draw.stamp()
    
def death(hp):
    if hp <=0:
        print ("You have lost the game")
        retry()
        
def play(health, power):
    draw.shape("circle")
    draw.color ("red")
    print ("Health: ", health)
    print ("Power: ", power)
    direction = raw_input("Would you like to go up, down, left, or right: ")
    if(direction == "down"):
        power += 10
        health -= 50
        turnDown()
        print ("You encountered a dragon and the dragon deals 50 damage to you")
        death(health)
        print("You attack and deal", power, " damage to it" )
        print("The dragon leaves")
        print("You level up you now deal ",power, " damage to enemies" )
        play(health, power)
    elif(direction == "left"):
        power += 10
        health -= 30
        turnLeft()
        print ("You encountered a vampire and the vampire deals 30 damage to you")
        death(health)
        print("You attack and deal", power, " damage to it")       
        print("The vampire disappears ")
        print("You level up you now deal ",power, " damage to enemies" )
        play(health, power)
    elif(direction == "right"):
        power += 10
        health -= 10
        turnRight()
        print ("You encountered an evil knight and the evil knight deals 10 damage to you")
        death(health)
        print("You attack and deal", power, " damage to it")
        print("The evil knight flees")
        print("You level up you now deal ",power, " damage to enemies" )
        play(health, power)
    elif(direction == "up"):
        health = 100
        turnUp()
        print ("You encountered a good wizard")
        print("The good wizard heals all of your hp")
        print("The wizard teleports away")
        print("You now have", health, "HP")
        play(health, power)
    else:
        print ("Please type a valid choice in lowercase ")
        play(health, power)
play(100, 50)

