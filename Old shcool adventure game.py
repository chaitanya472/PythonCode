
print("Welcome to the jungle. Survive if you can")
print()


    
def choice(health, damage):
    print("You have ", health, " HP")
    print("You do ", damage, " damage to the enemies")
    print("________________")

    direction = input("Pick a direction (r, l, u, d): ")
    if(direction == "r"):
        damage += 10
        health -= 50
        print ("You encountered a dragon and the dragon deals 50 damage to you")
        print("You attack and deal", damage, " damage to it" )
        print("The dragon leaves")
        print("You level up you now deal ",damage, " damage to enemies" )
        choice(health, damage)
    elif(direction == "u"):
        damage += 10
        health -= 30
        print ("You encountered a vampire and the vampire deals 30 damage to you")
        print("You attack and deal", damage, " damage to it")       
        print("The vampire disappears ")
        print("You level up you now deal ",damage, " damage to enemies" )
        choice(health, damage)
    elif(direction == "l"):
        damage += 10
        health -= 10
        KickCount = 0
        print ("You encountered an evil knight and the evil knight deals 10 damage to you")
        print("You attack and deal", damage, " damage to it")
        print("The evil knight flees")
        print("You level up you now deal ",damage, " damage to enemies" )
        choice(health, damage)
    elif(direction == "d"):
        health = 100
        print ("You encountered a good wizard")
        print("The good wizard heals all of your hp")
        print("The wizard teleports away")
        print("You now have", health, "HP")
        choice(health, damage)
    else:
        print ("Please enter a valid choice (r,l,u,d)")
        choice(health, damage)
choice(100, 50)
