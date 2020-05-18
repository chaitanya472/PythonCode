#Skill 1 how to turn values into strings
bitcoin = 9000
bitValue = str(bitcoin)
print("The value of a bitcoin is", bitValue)

#Skill 2 While loops
i=0
while i < 5:
    print (str(i))
    i += 1
while True:
    print (i)
    if (i == 10):
        break
    else:
        i+=1

#Skill 3 lists
Meals = [ "Breakfest", "Lunch", "Snack", "Dinner"]
print(Meals)
print(Meals[2])

# Skill 4 random.choice()
import random
mealType =random.choice(Meals)
print (mealType)

# Skill 5 String Replacement - %s

print ("I will have %s"% mealType)
