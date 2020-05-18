import random
Riddles =["""I am a fruit. I am tasty and provide lots of energy.
You can also find me in a calendar. What am I?""", """What can travel around
the world while staying in a corner""", """What can you hear but not touch or
see and yet control""", """It can be cracked, It can be made, It can be told,
it can be played. What is it?""", """It's red, blue, purple and green, no one
can reach it, not even the queen. What is it?"""]

riddle2 =[ Riddles[0], Riddles[1], Riddles[2], Riddles[3], Riddles[4]]

An =['date', 'stamp', 'voice', 'joke', 'rainbow']
right = 0

def askRiddle(type):
    global right
    check = ("true")
    if type == Riddles[0]:
        answer = An[0]
    elif type == Riddles[1]:
        answer = An[1]
    elif type == Riddles[2]:
        answer = An[2]
    elif type == Riddles[3]:
        answer = An[3]
    elif type == Riddles[4]:
        answer = An[4]
    riddle2.remove(type)

    print(type)
    for Attempt in range(1, 4):
        At = str(Attempt) + ":"
        At = raw_input("Attempt # %s" %At)
        if (At == answer):
            print("That is correct")
            right += 1
            break
        else:
            print("Sorry that is incorrect")
            if (Attempt == 3):
                print("Unfortunately you are out of attepts the answer was %s" %answer)
                break

print("""Welcome to the riddle show the show that only asks you riddles. The
rules of this show are simple we'll ask you 1 of 5 riddles and give you 3 chances
to answer the riddle. all answers should be lowercase and only be one word.""")
raw_input("Press enter when you are ready to begin")

print("Riddle #1")
check = "false"
while True:
    if not riddle2:
        print("Congrats you have finished all of the riddles and got ", right, "answers correct")
        break
    else:
        riddle = random.choice(riddle2)
        askRiddle(riddle)
        if (check == "true"):
            print("On to the next riddle")


